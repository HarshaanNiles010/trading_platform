"""simplyGold URL Configuration

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
from django.urls import path,include 

urlpatterns = [
    # for main page
    path('',include("mainPage.urls")),
    # for admin page
    path('admin/', admin.site.urls),
    # for silver
    path('silver/',include("silverPage.urls")),
    # for gold
    path('gold/',include("goldPage.urls")),
    # for diamond
    path('diamond/',include("diamondPage.urls")),
    # for new users
    path('users/',include("users.urls")),
    path('users/',include('django.contrib.auth.urls')),
    path('payment/',include("payment.urls")), 
    path('accounts/', include('allauth.urls')),
]
