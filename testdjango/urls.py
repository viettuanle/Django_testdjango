"""testdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
from testdjango.views import home, page
from testdjango import views
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', home),
    url(r'^sub/', views.subpage),
    url(r'^page/', page),
    url(r'^simpletemplate',views.httptemplate),
    url(r'^renderex/', views.renderexample),
    url(r'^base/', views.renderbase),
    url(r'^index/', views.renderindex),
    url(r'^welcome/', views.rendervariable),
    url(r'^filter/', views.filter_ex),
    url(r'^vonglap/', views.vonglap_ex),
    url(r'^vonglap2/', views.vonglap_ex2),
    url(r'^vonglap3/', views.vonglap_ex3),
    url(r'^include_ex/', views.include_ex),
]
