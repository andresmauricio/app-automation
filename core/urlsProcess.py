from django.conf.urls import url
from  core.views import CreateProcess

urlpatterns = [

    url(r'^nuevo/', CreateProcess.as_view(), name= 'crear_proceso')

    
]