from django.urls import path
from .views import login_view, logout_view, admin_dashboard, auxiliar_dashboard, dentista_dashboard, paciente_dashboard

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("dashboard/admin/", admin_dashboard, name="admin_dashboard"),
    path("dashboard/auxiliar/", auxiliar_dashboard, name="auxiliar_dashboard"),
    path("dashboard/dentista/", dentista_dashboard, name="dentista_dashboard"),
    path("dashboard/paciente/", paciente_dashboard, name="paciente_dashboard"),
]

