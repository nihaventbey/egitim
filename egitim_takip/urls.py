from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

class LogoutGetView(LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

urlpatterns = [
    path('', views.ana_sayfa, name='ana_sayfa'),
    path('merkez/<int:pk>/', views.egitim_merkezi_detay, name='egitim_merkezi_detay'),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
    path("login/", LoginView.as_view(
        template_name="login.html",
        next_page="/dashboard/"
    ), name="login"),
]