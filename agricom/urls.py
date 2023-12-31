"""
URL configuration for agricom project.

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
from django.urls import path, re_path

from reporter.models import WaterConsumption

import reporter.views
from reporter.views import waterconsumption_dataset, top10_consumers

urlpatterns = [
    re_path(r'^$', reporter.views.home, name='home'),
    re_path(r'^waterconsumption_data/$', waterconsumption_dataset, name='waterconsumption'),
    re_path(r'^top10_consumers/$', top10_consumers, name='top10_consumers'),
    path('admin/', admin.site.urls)
]
