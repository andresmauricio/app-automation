# Generated by Django 2.2.3 on 2019-08-02 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_material_id_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='queality',
            new_name='quality',
        ),
        migrations.RenameField(
            model_name='process',
            old_name='id',
            new_name='id_process',
        ),
        migrations.RenameField(
            model_name='productfinisehd',
            old_name='id',
            new_name='id_product_finished',
        ),
    ]
