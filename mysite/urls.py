from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    
    path('admin/',admin.site.urls),
    path('about/',views.about),
    path('articles',include('articles.urls')),
    path('',views.home),
]
urlpatterns += staticfiles_urlpatterns()
