from django.shortcuts import render

from core.models import Factory
from core.forms import FactoryForm
from django.views.generic import CreateView, UpdateView, ListView, DeleteView



class CreateFactory(CreateView):
    model = Factory
    form_class = FactoryForm
    template_name = 'config/create_factory.html'
    


