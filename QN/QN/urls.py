"""QN URL Configuration

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
from django.urls import path,include,re_path
from q1 import views as qv
from django import views as dv
from . import settings#导入settings.py
urlpatterns = [
    path("",qv.index,name=""),#首页
    path("content/",include('q1.urls')), #内容
    re_path(r'^static/(?P<path>.*)$', dv.static.serve, {"document_root": settings.STATIC_ROOT}),#显示静态文件
]
