from django.db import models
from django.contrib.auth.models import User



class Factory(models.Model):

    id = models.AutoField(primary_key = True)
    name_factory = models.CharField( max_length=50)
    city = models.CharField( max_length=50)
    average_production = models.IntegerField()
    id_machine = models.ManyToManyField('Machine') 

    def __str__(self):
        return self.name_factory
    

class Machine(models.Model):

    id= models.AutoField(primary_key = True)
    name_machine = models.CharField(max_length=50)
    process_machine = models.CharField(max_length=50)
    id_process = models.ManyToManyField('Process')

    def __str__(self):
        return self.name_machine
    

class Process(models.Model):
    
    id_process = models.AutoField(primary_key = True)
    name_process = models.CharField( max_length=50)
    type_process = models.CharField( max_length=50)
    temperature_initial = models.IntegerField()
    temperature_ideal = models.IntegerField()
    temperature_cooling = models.IntegerField()
    time_process = models.IntegerField()
    color_process = models.CharField(max_length=50)

    id_machine = models.ManyToManyField('Machine')

    def __str__(self):
        return self.name_process


class ProductFinisehd(models.Model):

    id_product_finished = models.AutoField(primary_key = True)
    name_product = models.CharField( max_length=50)
    id_process = models.ManyToManyField('Process')
    id_material =models.ForeignKey('Material',on_delete=models.CASCADE)

    def __str__(self):
        return self.name_product    
            

class Material(models.Model):
    id_material = models.AutoField(primary_key = True)
    name_material = models.CharField(max_length=50)

    def __str__(self):
        return self.name_material 
    

class Order(models.Model):
    id_order = models.AutoField(primary_key = True)
    quality = models.IntegerField()
    id_material = models.ManyToManyField('Material')

    def __str__(self):
        return self.quality

class ProcessMachineForTime(models.Model):
    id_time_process = models.AutoField(primary_key= True)
    time_process = models.IntegerField()
    id_machine = models.ForeignKey('Machine',on_delete=models.CASCADE)
    id_process = models.ForeignKey('Process',on_delete=models.CASCADE)

    def __str__(self):
        return self.time_process
    
    

    
    
