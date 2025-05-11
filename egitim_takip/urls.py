
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ana_sayfa, name='ana_sayfa'),
    path('merkez/<int:pk>/', views.egitim_merkezi_detay, name='egitim_merkezi_detay'),
    path("dashboard/", views.dashboard, name="dashboard"),
]