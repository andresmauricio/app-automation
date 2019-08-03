from django.conf.urls import url
from  core.views import CreateFactory

urlpatterns = [

    
    url(r'^nueva/', CreateFactory.as_view(), name= 'crear_fabrica')

    
]
