from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('api/details/', views.details, name="details"),
    path('api/details/<int:id>/', views.UniqueView, name="detailsview"),
    path('api/details/delete/<int:id>/', views.deletedata, name="deletedata")
]
