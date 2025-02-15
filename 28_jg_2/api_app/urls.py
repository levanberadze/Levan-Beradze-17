from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('persons/', views.PersonListApiView.as_view()),
    path('persons/<int:pk>', views.PersonDetailApiView.as_view()),
    path('cities/', views.CityListApiView.as_view()),
    path('cities/<int:pk>', views.CityDetailApiView.as_view()),
]
