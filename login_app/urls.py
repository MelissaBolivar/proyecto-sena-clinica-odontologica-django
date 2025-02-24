from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("dashboard/admin/", views.admin_dashboard, name="admin_dashboard"),
    path("dashboard/auxiliar/", views.auxiliar_dashboard, name="auxiliar_dashboard"),
    path("gestion_pacientes/", views.gestion_pacientes, name="gestion_pacientes"),
    path("dashboard/dentista/", views.dentista_dashboard, name="dentista_dashboard"),
    path("dashboard/paciente/", views.paciente_dashboard, name="paciente_dashboard"),
    path('gestion-usuarios/', views.gestion_usuarios, name='gestion_usuarios'),
    path('crear-usuario/', views.crear_usuario, name='crear_usuario'),
    path('editar-usuario/<int:user_id>/', views.editar_usuario, name="editar_usuario"),
    path("eliminar-usuario/<int:usuario_id>/", views.eliminar_usuario, name="eliminar_usuario"),
    path("gestion-citas/", views.gestion_citas, name="gestion_citas"),
    path("crear-citas/<int:paciente_id>/", views.crear_cita, name="crear_citas"),
    path("ver_citas_pendientes/<int:paciente_id>/", views.ver_citas_pendientes, name="ver_citas_pendientes"),
    path("editar_cita/<int:cita_id>/", views.editar_cita, name="editar_cita"),
    path("eliminar_cita/<int:cita_id>/", views.eliminar_cita, name="eliminar_cita"),
]