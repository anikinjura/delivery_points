# Generated by Django 5.0.6 on 2024-08-16 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pickup_points', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pickuppoint',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]