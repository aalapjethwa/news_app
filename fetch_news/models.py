from django.db import models


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


class MapDBParameter(models.Model):
    DB_PARAMETER = (
        ("title", "title"),
        ("categories", "categories"),
        ("description", "description"),
        ("content", "content")
    )
    news_api = models.ForeignKey(
        NewsAPI, on_delete=models.CASCADE, related_name="map_db_parameter"
    )
    api_parameter = models.CharField(max_length=100)
    db_parameter = models.CharField(
        max_length=100, choices=DB_PARAMETER, db_index=True
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
    content = models.TextField()
    last_updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
