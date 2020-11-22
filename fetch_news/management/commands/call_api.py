import json
import time

import requests

from django.conf import settings
from fetch_news.models import NewsAPI, Article, Category
from django.core.management.base import BaseCommand


def set_categories(bulk_ref):
    categories = Category.objects.values('id','name')
    for article in Article.objects.filter(bulk_ref=bulk_ref):
        search_text = article.full_search_text()
        category_list = []
        for cat in categories:
            if cat['name'].lower() in search_text.lower():
                category_list.append(cat['id'])
            if cat['name'].lower() == "general":
                default_id = cat['id']
        if not category_list:
            category_list = [default_id]
        article.categories.add(*category_list)


def load_articles(map_db_parameter, response_json):
    bulk_ref = time.time()
    article_list = []
    for text in response_json:
        try:
            query_dict = {}
            for p in map_db_parameter:
                query_dict[p["db_parameter"]] = text.get(p["api_parameter"])
            article_list.append(
                Article(
                    title=query_dict.get("title"),
                    description=query_dict.get("description"),
                    content=query_dict.get("content"),
                    bulk_ref=bulk_ref,
                )
            )
        except Exception as e:
            print("Excpetion occured in fetch data:", e)
    Article.objects.bulk_create(article_list)
    print("Articles created")
    set_categories(bulk_ref)


class Command(BaseCommand):

    def handle(self, *args, **options):
        for api in NewsAPI.objects.all():
            url = api.request_url()
            response = requests.get(url)
            if response.status_code == 200:
                response_text = json.loads(response.text)
                if response_text.get("articles") and api.map_db_parameter.exists():
                    map_db_parameter = list(api.map_db_parameter.filter(
                        active=True
                    ).values('db_parameter', 'api_parameter'))
                    load_articles(map_db_parameter, response_text['articles'])
                else:
                    print("response_text: ", response_text)
            else:
                print("status_code: ", response.status_code)
