from django import forms

from core.models import Factory, Machine, Process, ProductFinisehd, Material, Order, ProcessMachineForTime

class FactoryForm(forms.ModelForm):
    class Meta:
        model = Factory
        fields = [
          'id' ,
          'name_factory',
          'city' ,
          'average_production' ,
          'id_machine' ,
        ]
        label = {
          'id':'Identificacion' ,
          'name_factory':'Nombre de la fabrica',
          'city' :'Ciudad',
          'average_production':'Produccion Promedio' ,
          'id_machine':'Maquina' ,
        }
        widets={
          'id': forms.TextInput(attrs={'class': 'form-control'}) ,
          'name_factory': forms.TextInput(attrs={'class': 'form-control'}),
          'city': forms.TextInput(attrs={'class': 'form-control'}) ,
          'average_production': forms.TextInput(attrs={'class': 'form-control'}) ,
          'id_machine': forms.SelectMultiple(attrs={'class': 'form-control'}) ,
            
        }

class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = [
          'id' ,
          'name_machine',
          'process_machine' ,
        ]
        label = {
          'id':'Identificacion' ,
          'name_machine':'Nombre Maquina',
          'process_machine':'Proceso Maquina',
        }
        widets={
          'id': forms.TextInput(attrs={'class': 'form-control'}) ,
          'name_machine': forms.TextInput(attrs={'class': 'form-control'}),
          'process_machine': forms.TextInput(attrs={'class': 'form-control'}) ,  
        }

class ProcessForm(forms.ModelForm):
    class Meta:
        model = Process
        fields = [
          'id_process' ,
          'name_process',
          'type_process',
          'temperature_initial',
          'temperature_ideal',
          'temperature_cooling',
          'time_process',
          'color_process',
          'id_machine'
        ]
        label = {
          'id_process': 'Identificacion',
          'name_process':'Nombre del Proceso',
          'type_process':'Tipo de Proceso',
          'temperature_initial': 'Temperatura Inicial',
          'temperature_ideal':'Temperatura Ideal',
          'temperature_cooling': 'Temperatura de Enfriamiento',
          'time_process':'Tiempo de Proceso',
          'color_process': 'Color',
          'id_machine' :'Maquina'
          
        }
        widets={

          'id_process': forms.TextInput(attrs={'class':'form-control'}),
          'name_process': forms.TextInput(attrs={'class':'form-control'}),
          'type_process': forms.TextInput(attrs={'class':'form-control'}),
          'temperature_initial':forms.IntegerField(),
          'temperature_ideal':forms.IntegerField(),
          'temperature_cooling':forms.IntegerField(),
          'time_process':forms.IntegerField(),
          'color_process': forms.TextInput(attrs={'class':'form-control'}),
          'id_machine':forms.Select(attrs={'class':'form-control'})
        }

class ProductFinisehdForm(forms.ModelForm):
    class Meta:
            model = ProductFinisehd
            fields = [
              'id_product_finished' ,
              'name_product',
              'process' ,
              'material' , 
            ]
            label = {
              'id_product_finished':'Identificacion' ,
              'name_product':'Nombre del Producto',
              'process' :'Procesos',
              'material':'Material' ,
            }
            widets={
              'id_product_finished': forms.TextInput(attrs={'class': 'form-control'}) ,
              'name_product': forms.TextInput(attrs={'class': 'form-control'}),
              'process': forms.SelectMultiple(attrs={'class': 'form-control'}) ,
              'material': forms.Select(attrs={'class': 'form-control'}) ,
                
            }

class MaterialForm(forms.ModelForm):
    class Meta:
            model = Material
            fields = [
              'id_material' ,
              'name_material',
            ]
            label = {
              'id_material':'Identificacion' ,
              'name_material':'Nombre del Material',
           
            }
            widets={
              'id_material': forms.TextInput(attrs={'class': 'form-control'}) ,
              'name_material': forms.TextInput(attrs={'class': 'form-control'}),
             
                
            }

class OrderForm(forms.ModelForm):
    class Meta:
            model = Order
            fields = [
              'id_order' ,
              'quality',
              'id_material'
            ]
            label = {
              'id_order':'Identificacion' ,
              'quality':'Cantidad',
              'id_material':'Material'
           
            }
            widets={
              'id_order': forms.TextInput(attrs={'class': 'form-control'}) ,
              'quality': forms.IntegerField(),
              'id_material' : forms.Select(attrs={'class': 'form-control'})
             
                
            }

class ProcessMachineForTimeForm(forms.ModelForm):

    class Meta:
            model = ProcessMachineForTime
            fields = [
              'id_time_process' ,
              'time_process',
              'machine',
              'process'
            ]
            label = {
              'id_time_process':'Identificacion' ,
              'time_process':'Tiempo',
              'machine':'Material',
              'process': 'Proceso'
           
            }
            widets={
              'id_time_process': forms.TextInput(attrs={'class': 'form-control'}) ,
              'time_process': forms.IntegerField(),
              'machine' : forms.Select(attrs={'class': 'form-control'}),
              'process': forms.Select(attrs={'class': 'form-control'}),
             
                
            }