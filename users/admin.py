from django.contrib import admin

from users.models import Profile

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name', 'position')