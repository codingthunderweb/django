from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    
    path('',views.article_list),
    url('(?P<slug>[\w-]+)',views.article_detail),
]

