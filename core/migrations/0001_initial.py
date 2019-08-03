# Generated by Django 2.2.3 on 2019-08-03 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_machine', models.CharField(max_length=50)),
                ('process_machine', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id_material', models.AutoField(primary_key=True, serialize=False)),
                ('name_material', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id_process', models.AutoField(primary_key=True, serialize=False)),
                ('name_process', models.CharField(max_length=50)),
                ('type_process', models.CharField(max_length=50)),
                ('temperature_initial', models.IntegerField()),
                ('temperature_ideal', models.IntegerField()),
                ('temperature_cooling', models.IntegerField()),
                ('time_process', models.IntegerField()),
                ('color_process', models.CharField(max_length=50)),
                ('id_machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Machine')),
            ],
        ),
        migrations.CreateModel(
            name='ProductFinisehd',
            fields=[
                ('id_product_finished', models.AutoField(primary_key=True, serialize=False)),
                ('name_product', models.CharField(max_length=50)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Material')),
                ('process', models.ManyToManyField(to='core.Process')),
            ],
        ),
        migrations.CreateModel(
            name='ProcessMachineForTime',
            fields=[
                ('id_time_process', models.AutoField(primary_key=True, serialize=False)),
                ('time_process', models.IntegerField()),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Machine')),
                ('process', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Process')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id_order', models.AutoField(primary_key=True, serialize=False)),
                ('quality', models.IntegerField()),
                ('id_material', models.ManyToManyField(to='core.Material')),
            ],
        ),
        migrations.CreateModel(
            name='Factory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_factory', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('average_production', models.IntegerField()),
                ('id_machine', models.ManyToManyField(to='core.Machine')),
            ],
        ),
    ]
