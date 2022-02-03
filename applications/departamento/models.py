from django.db import models

# Create your models here.

class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    short_name = models.CharField('Nombre corto' , max_length=50)
    active = models.BooleanField('Anulado', default=False)

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
        ordering = ['-name']

    def __str__(self):
        return str(self.id) + ' - ' + self.name + ' - ' +  self.short_name