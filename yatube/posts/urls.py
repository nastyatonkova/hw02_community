# posts/urls.py
from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    # main page
    path('', views.index, name='index'),
    # page for a certain group
    path('group/<slug:slug>/', views.group_posts, name='group_list')
]
