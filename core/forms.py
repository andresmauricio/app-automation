from django import forms

from core.models import Factory

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
