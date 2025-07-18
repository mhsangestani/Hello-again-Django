from django.urls import path
from .views import *
from blog.feeds import LatestEntriesFeed


app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='index'),
    path('<int:pid>', blog_single_view, name='single'),
    path('category/<str:cat_name>', blog_view, name='category'),
    path('tag/<str:tag_name>', blog_view, name='tag'),

    path('author/<str:author_username>', blog_view, name='author'),
    path('search/', blog_search_view, name='search'),
    path("rss/feed/", LatestEntriesFeed())


]