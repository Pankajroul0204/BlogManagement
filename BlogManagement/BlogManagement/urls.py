"""
URL configuration for BlogManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from BlogManagement import views
from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
        path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('category/', views.category, name='category'),
    path('blog-details/', views.blog_details, name='blog_details'),
    path('author-page/', views.author_page, name='author_page'),
    path('contacts/', views.contact, name='contacts'),
    path('search-result/', views.search_result, name='search_result'),
    path('not-found/', views.not_found, name='not_found'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
