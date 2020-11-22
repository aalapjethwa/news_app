from django.shortcuts import render
from django.views.generic import ListView, DetailView

from fetch_news.models import Article


class ArticleListView(ListView):
    model = Article
    paginate_by = 10
    context_object_name = "article_list"
    template_name  = "fetch_news/article_list.html"

class ArticleDetailView(DetailView):
    model = Article
