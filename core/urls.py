from django.conf.urls import url
from  core.views     import CreateFactory

urlpatterns = [

    url(r'^nuevo/', CreateFactory.as_view(), name= 'crear_fabrica')
    
]
