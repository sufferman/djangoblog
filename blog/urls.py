
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
    path('about/', views.about),
    path('contact/', views.contact),
    path('services/', views.services),
    path('articles/', include('articles.urls')),
    
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)