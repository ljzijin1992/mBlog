from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'blog.views.index', name='index'),
    url(r'^(?P<article_id>\d+)/$','blog.views.detail',name='detail'),

)
