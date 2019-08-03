from django.conf.urls import url
from  core.views import  CreateMachine

urlpatterns = [

    url(r'^nueva/', CreateMachine.as_view(), name= 'crear_maquina')

    
]
