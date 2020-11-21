from django.db import models
from constants.fetch_news import DB_PARAMETERS


class NewsAPI(models.Model):
    api_name = models.CharField(max_length=100, unique=True)
    api_url = models.URLField()
    api_parameters = models.CharField(max_length=500, null=True, blank=True)
    api_key_paramter = models.CharField(max_length=100, null=True, blank=True)
    api_key_token = models.CharField(max_length=200, null=True, blank=True)
    active = models.BooleanField(default=True, db_index=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.api_name

    class Meta:
        verbose_name = "NewsAPI"
        verbose_name_plural = "NewsAPIs"

    def request_url(self):
        url = f"{self.api_url}?"
        if self.api_parameters:
            url += f"{self.api_parameters}"
        if self.api_key_paramter and self.api_key_token:
            url += f"&{self.api_key_paramter}={self.api_key_token}"
        return url


class MapDBParameter(models.Model):
    news_api = models.ForeignKey(
        NewsAPI, on_delete=models.CASCADE, related_name="map_db_parameter"
    )
    api_parameter = models.CharField(max_length=100)
    db_parameter = models.CharField(
        max_length=100, choices=DB_PARAMETERS, db_index=True
    )
    active = models.BooleanField(default=True, db_index=True)

    def __str__(self):
        return f"{self.news_api.api_name} api's parameter"


class Category(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField()
    last_updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Article(models.Model):
    title = models.CharField(max_length=500)
    categories = models.ManyToManyField(
        Category, blank=True, related_name="articles"
    )
    description = models.TextField()
    content = models.TextField(null=True, blank=True)
    bulk_ref = models.CharField(max_length=50, null=True, blank=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def full_search_text(self):
        return self.title + self.description + (self.content or "")

    def __str__(self):
        return self.title
