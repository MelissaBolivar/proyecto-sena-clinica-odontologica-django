from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Administrador'),
        ('auxiliar', 'Auxiliar Administrativo'),
        ('dentista', 'Dentista'),
        ('paciente', 'Paciente'),
    ]

    nombre_completo = models.CharField(max_length=255)
    numero_documento = models.CharField(max_length=20, unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='paciente')

    def __str__(self):
        return self.username
    
class Cita(models.Model):
    paciente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="citas_paciente")
    dentista = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="citas_dentista")
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.TextField()
    estado = models.CharField(
        max_length=20,
        choices=[("pendiente", "Pendiente"), ("confirmada", "Confirmada"), ("cancelada", "Cancelada")],
        default="pendiente"
    )

    def __str__(self):
        return f"Cita de {self.paciente.username} con {self.dentista.username if self.dentista else 'Sin asignar'} el {self.fecha} a las {self.hora}"