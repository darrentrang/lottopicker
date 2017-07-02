"""{{ project_name }} URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/{{ docs_version }}/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #url(r'^adminadmin/', admin.site.urls),
    url(r'^$', views.home, name="home"),
    url(r'^powerball/', views.powerball_option, name="powerball_option"),
    url(r'^megamillions/', views.megamillions_option, name="megamillions_option"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
