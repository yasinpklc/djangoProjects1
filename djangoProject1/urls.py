"""djangoProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.urls import path,include
from django.conf import settings
from home import views

urlpatterns = [
    path('home/', include('home.urls')),
    path('Library/', include('Library.urls')),
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('hakkimizda/', views.hakkimizda, name='hakkimizda'),
    path('oduncverme/', views.oduncverme, name='oduncverme'),
    path('iletisim/', views.iletisim, name='iletisim'),
    path('sikcasorulansorular/', views.sikcasorulansorular, name='sikcasorulansorular'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),


]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)