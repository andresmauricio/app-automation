
from django.contrib import admin
from django.urls import path

from django.conf.urls import url, include


from users import views as users_views 
from control import views as control_views 


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', users_views.login_view, name='login'),
    path('signup/', users_views.signup_view, name="signup"),
    path('home/', control_views.dashboard_view, name='dash'),

    url(r'^fabricas/',include('core.urls'))
    
]
