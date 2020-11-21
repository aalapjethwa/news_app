from django.db import models


class NewsAPI(models.Model):
    api_name = models.CharField(max_length=100, unique=True)
    api_url = models.URLField()
    api_parameters = models.CharField(max_length=500, null=True, blank=True)
    api_key_paramter = models.CharField(max_length=100, null=True, blank=True)
    api_key_token = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.api_name


class Category(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=500)
    categories = models.ManyToManyField(
        Category, blank=True, related_name="articles"
    )
    description = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.title
