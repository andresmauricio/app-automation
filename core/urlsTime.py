from django.conf.urls import url
from  core.views import CreateProcessMachineForTime

urlpatterns = [

    url(r'^nuevo/', CreateProcessMachineForTime.as_view(), name= 'crear_tiempo')

]