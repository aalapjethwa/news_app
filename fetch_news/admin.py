from django.contrib import admin

from fetch_news.models import *


class MapDBParameterInline(admin.TabularInline):
    model = MapDBParameter
    extra = 0


class NewsAPIAdmin(admin.ModelAdmin):
    inlines = [MapDBParameterInline,]


class CategoryAdmin(admin.ModelAdmin):
    pass


class ArticleAdmin(admin.ModelAdmin):
    pass


admin.site.register(NewsAPI, NewsAPIAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
