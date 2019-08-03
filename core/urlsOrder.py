from django.conf.urls import url
from  core.views import  CreateOrder

urlpatterns = [

    url(r'^nueva/', CreateOrder.as_view(), name= 'crear_orden')

    
]