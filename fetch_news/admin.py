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
    exclude = ('bulk_ref', )
    list_display = ('title', 'get_categories')
    list_filter = ('last_updated_at', 'created_at', 'categories__name')

    def get_categories(self, obj):
        return list(obj.categories.values_list('name', flat=True))
    get_categories.short_description = "Categories"


admin.site.register(NewsAPI, NewsAPIAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(TaskQueue)
