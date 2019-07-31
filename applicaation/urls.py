
from django.contrib import admin
from django.urls import path
from users import views as users_views 

urlpatterns = [

    path('admin/', admin.site.urls),
    path('users/login/', users_views.login_view, name='login')
]
