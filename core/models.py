from django.db import models
from django.contrib.auth.models import User



class Factory(models.Model):

    id = models.AutoField(primary_key = True)
    name_factory = models.CharField( max_length=50)
    city = models.CharField( max_length=50)
    average_production = models.IntegerField()
    id_machine = models.ManyToManyField('Machine') 

class Machine(models.Model):

    id= models.AutoField(primary_key = True)
    name_machine = models.CharField(max_length=50)
    process_machine = models.CharField(max_length=50)
    id_process = models.ManyToManyField('Process')

class Process(models.Model):
    
    id_process = models.AutoField(primary_key = True)
    name_process = models.CharField( max_length=50)
    id_machine = models.ManyToManyField('Machine')

class ProductFinisehd(models.Model):

    id_product_finished = models.AutoField(primary_key = True)
    name_product = models.CharField( max_length=50)
    id_process = models.ManyToManyField('Process')
    id_material =models.ForeignKey('Material',on_delete=models.CASCADE)

class Material(models.Model):
    id_material = models.AutoField(primary_key = True)
    name_material = models.CharField(max_length=50)

class Order(models.Model):
    id_order = models.AutoField(primary_key = True)
    quality = models.IntegerField()
    id_material = models.ManyToManyField('Material')

    
    
