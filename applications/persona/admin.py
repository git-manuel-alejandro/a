from django.contrib import admin
from .import models

# Register your models here.

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'job', 'departamento')
    search_fields = ('last_name',)
    list_filter = ('job','habilidades',)
    filter_horizontal = ('habilidades',)
    #https://django-ckeditor.readthedocs.io/en/latest/



    def full_name(self, obj):
        name = obj.first_name +" " + obj.last_name
        return name

admin.site.register(models.Empleado , EmpleadoAdmin)
admin.site.register(models.Habilidades)
