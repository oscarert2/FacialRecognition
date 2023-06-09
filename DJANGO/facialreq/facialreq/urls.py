"""
URL configuration for facialreq project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from facialreq.views import home 
from . import views
from .views import my_view
from facialreq.views import results

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('save_image/', views.save_image, name='save_image'),
    path('my-url/', my_view, name='my_view'),
    path('results', results, name='results'),
]
