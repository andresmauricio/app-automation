#Django
from django.contrib import admin

#Models
from core.models import Factory, Machine, Process, ProductFinisehd, Material, Order, ProcessMachineForTime


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ('name_factory', 'city','average_production')

@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ('name_machine', 'process_machine')

@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = ('id_process','name_process')

@admin.register(ProductFinisehd)
class ProductFinisehdAdmin(admin.ModelAdmin):
    list_display = ('id_product_finished','name_product')

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('id_material','name_material')
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id_order','quality')

@admin.register(ProcessMachineForTime)
class ProcessMachineAdmin(admin.ModelAdmin):
    list_display = ('id_time_process', 'time_process')




