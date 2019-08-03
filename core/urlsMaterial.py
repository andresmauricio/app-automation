from django.conf.urls import url
from  core.views import  CreateMaterial

urlpatterns = [

    url(r'^nueva/', CreateMaterial.as_view(), name= 'crear_material')

    
]