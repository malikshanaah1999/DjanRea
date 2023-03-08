from django.contrib import admin
from django.urls import path, re_path
from . import views



urlpatterns = [
    path('tweet/<int:tweet_id>', views.tweet_detail_view, name= 'tweet_detail_view'),
    path('api/tweet/<int:tweet_id>/delete', views.tweet_delete_view, name= 'tweet_delete_view'),
    path('', views.home_view, name= 'home_view'),
    path('tweets/', views.tweet_list_view, name= 'tweet_list_view'),
    path('tweet-create', views.tweet_create_view, name= 'tweet_create_view')
]
