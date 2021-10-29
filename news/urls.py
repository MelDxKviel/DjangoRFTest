from django.urls import path

from news.views import (
    ArticleListView,
    ArticleCreateView,
    ArticleRetrieveUpdateDestroyView,
    ArticleListByTypeView,
    TypeListView,
    TypeRetrieveUpdateDestroyView
)

urlpatterns = [
    path('articles/', ArticleListView.as_view()),
    path('articles/<int:pk>', ArticleRetrieveUpdateDestroyView.as_view()),
    path('articles/create', ArticleCreateView.as_view()),
    path('articles/type/<int:pk>', ArticleListByTypeView.as_view()),
    path('types/', TypeListView.as_view()),
    path('types/<int:pk>', TypeRetrieveUpdateDestroyView.as_view()),
]