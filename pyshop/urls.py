"""pyshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path, include
from products import views as v1
from userdata import views as v2
from carts import views as v3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/s/', v1.search, name='search'),
    path('register/', v2.register, name='register'),
    path('', include("django.contrib.auth.urls")),
    path('products/', include('products.urls')),
    path('', include('django.contrib.auth.urls')),
    url(r'^cart/(?P<slug>[\w-]+)/', v3.update_cart, name='update_cart'),
    path('cart/', v3.view, name='cart')
]
