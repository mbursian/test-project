"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from products import views
from django.conf.urls.static import static

urlpatterns = [
    # url(r'^landing123/', views.landing, name='landing'),
    url(r'^product/(?P<product_id>\w+)/$', views.product, name='product'),
    url(r'^complex_product/(?P<complex_product_id>\w+)/$', views.complex_product, name='complex_product'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
