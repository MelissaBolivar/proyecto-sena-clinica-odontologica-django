from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Administrador'),
        ('auxiliar', 'Auxiliar Administrativo'),
        ('dentista', 'Dentista'),
        ('paciente', 'Paciente'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='paciente')

    def __str__(self):
        return self.username