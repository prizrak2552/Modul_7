from django.urls import path

from .views import NewsList, NewsDetailView, ChangeNews, NewsSearch, AddNews, DeleteNews, new_subscribe, non_subscribe
from .views import IndexView


urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>/', NewsDetailView.as_view(), name='news_detail'),  # Ссылка на детали новости
    path('add/', AddNews.as_view(), name='news_add'),  # Ссылка на создание новости
    path('edit/<int:pk>', ChangeNews.as_view(), name='news_edit'),
    path('delete/<int:pk>', DeleteNews.as_view(), name='news_delete'),
    path('search/', NewsSearch.as_view(), name='news_searsh'),
    path('<int:pk>/new_subscribe/', new_subscribe, name='new_subscribe'),
    path('<int:pk>/non_subscribe/', non_subscribe, name='non_subscribe'),

    path('', IndexView.as_view()),
]
