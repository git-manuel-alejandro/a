from statistics import mode
from django.db import models

# Create your models here.

class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    short_name = models.CharField('Nombre corto' , max_length=50)
    active = models.BooleanField('Anulado', default=False)

    def __str__(self):
        return str(self.id) + ' - ' + self.name + ' - ' +  self.short_name