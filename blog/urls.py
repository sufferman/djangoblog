
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
    path('about/', views.about),
    path('contact/', views.contact),
    path('services/', views.services),
    path('articles/', include('articles.urls')),
    
]


urlpatterns += staticfiles_urlpatterns()