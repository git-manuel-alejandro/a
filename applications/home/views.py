from django.shortcuts import render
from django.views.generic import TemplateView, ListView , CreateView
from .import models

# Create your views here.

class Prueba(TemplateView):
    template_name = 'home/prueba.html'



class PruebaListView(ListView):
    template_name = "home/lista.html"
    context_object_name = 'lista'
    queryset = ['0', '10', '20','30']



class ListarPruebaListView(ListView):
    model = models.Prueba
    template_name = "home/lista_prueba.html"
    context_object_name = 'lista'


class PruebaCreateView(CreateView):
    model = models.Prueba
    template_name = "home/add.html"
    fields = '__all__'
