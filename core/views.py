from django.shortcuts import render

from core.models import Factory, Machine, Process, ProductFinisehd, Material, Order, ProcessMachineForTime
from core.forms import FactoryForm, MachineForm, ProcessForm, ProductFinisehdForm, MaterialForm, OrderForm, ProcessMachineForTimeForm
from django.views.generic import CreateView, UpdateView, ListView, DeleteView


#Crud Factories
class CreateFactory(CreateView):
    model = Factory
    form_class = FactoryForm
    template_name = 'config/create_factory.html'
    

#Crud Machine|
class CreateMachine(CreateView):
    model = Machine
    form_class = MachineForm
    template_name ='config/crudMachine/create_machine.html'

# Crud Process
class CreateProcess(CreateView):
    model = Process
    form_class =  ProcessForm
    template_name = 'config/crudProcess/create_process.html'

class CreateProductFinisehd(CreateView):
    model = ProductFinisehd
    form_class = ProductFinisehdForm
    template_name = 'config/crudProductFinish/create_pf.html'

class CreateMaterial(CreateView):
    model = Material
    form_class = MaterialForm
    template_name = 'config/crudMaterial/create_material.html'

class CreateOrder(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'config/crudOrder/create_order.html'

class CreateProcessMachineForTime(CreateView):
    model = ProcessMachineForTime
    form_class = ProcessMachineForTimeForm
    template_name = 'config/crudTime/create_time.html'
    