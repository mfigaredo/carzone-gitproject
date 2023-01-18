# from django.contrib import admin
from django.urls import path
from cars import views

urlpatterns = [
    path('', views.cars, name='cars'),
    path('detail/<int:pk>/', views.car_detail, name='car_detail'),
]