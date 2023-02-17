from django.contrib import admin
from django.urls import path, re_path
from . import views



urlpatterns = [
    path('tweet/<int:tweet_id>', views.tweet_detail_view, name= 'tweet_detail_view'),
    path('home_view/', views.home_view, name= 'home_view'),
    path('tweets/', views.tweet_list_view, name= 'tweet_list_view')
]
