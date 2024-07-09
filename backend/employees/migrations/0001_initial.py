# Generated by Django 5.0.6 on 2024-07-08 12:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agents', '0001_initial'),
        ('pickup_points', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_of_hire', models.DateField()),
                ('position', models.CharField(max_length=100)),
                ('role', models.CharField(choices=[('manager', 'Manager'), ('accountant', 'Accountant'), ('delivery_staff', 'Delivery Staff'), ('other', 'Other')], default='other', max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agents.agent')),
                ('default_pickup_point', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pickup_points.pickuppoint')),
            ],
        ),
    ]
