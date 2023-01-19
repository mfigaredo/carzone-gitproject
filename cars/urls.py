# from django.contrib import admin
from django.urls import path
from cars import views

urlpatterns = [
    path('', views.cars, name='cars'),
    path('<int:id>/', views.car_detail, name='car_detail'),
    path('inquiry/', views.cars, name='inquiry'),
]