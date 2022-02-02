from django.shortcuts import render
from django.views.generic import TemplateView, ListView

# Create your views here.

class Prueba(TemplateView):
    template_name = 'home/prueba.html'



class PruebaListView(ListView):
    template_name = "home/lista.html"
    context_object_name = 'lista'
    queryset = ['0', '10', '20','30']
