from django.conf.urls import url
from  core.views import  CreateProductFinisehd

urlpatterns = [

    url(r'^nuevo/', CreateProductFinisehd.as_view(), name= 'crear_prducto_terminado')

    
]