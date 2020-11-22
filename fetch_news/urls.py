from django.urls import path

from fetch_news.views import ArticleListView, ArticleDetailView

urlpatterns = [
    path('articles/list/', ArticleListView.as_view(), name="article_list"),
    path('articles/detail/<int:pk>/', ArticleDetailView.as_view(), name="article_detail"),
]
