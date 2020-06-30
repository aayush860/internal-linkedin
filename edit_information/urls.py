"""ThePremiumX URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import views


urlpatterns = [
    path('edit_info/', views.edit_info),
    path('edit_info/update_skills/', views.update_skills),
    path('edit_info/upload_image/', views.upload_image),
    path('edit_info/update_education/', views.update_education),
    path('edit_info/update_profession/', views.update_profession),
    path('edit_info/update_social/', views.update_social),
    path('edit_info/update_interest/', views.update_interest),
    path('edit_info/update_about/', views.update_about),
    path('edit_info/update_home/', views.update_home),
    path('edit_info/update_address/', views.update_address)

]
#path('ajax_calls/search/', views.autocompleteModel),