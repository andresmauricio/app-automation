# Generated by Django 2.2.3 on 2019-08-01 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factory',
            name='id_machine',
        ),
        migrations.AddField(
            model_name='factory',
            name='id_machine',
            field=models.ManyToManyField(to='core.Machine'),
        ),
    ]
