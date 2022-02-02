from django.db import models
from applications.departamento.models import Departamento

# Create your models here.

JOB_CHOICES = [
    ('0', 'CONTADOR'),
    ('1', 'ADMINISTRADOR'),
    ('2', 'ECONOMISTA'),
    ('3', 'Django Dev'),
]

class Empleado(models.Model):
    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    job = models.CharField('Trabajo' ,max_length=51, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento , on_delete=models.CASCADE)
    # image = models.ImageField()

    def __str__(self):
        return self.first_name + " " + self.last_name