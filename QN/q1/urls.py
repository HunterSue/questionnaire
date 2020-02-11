from django.contrib import admin
from django.urls import path
from q1 import views
urlpatterns = [
    path('add_massage/',views.add_massage,name="add_massage"),#给Ajax上传代码的路径
]
