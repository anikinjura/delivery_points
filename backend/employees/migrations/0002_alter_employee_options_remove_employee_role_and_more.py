# Generated by Django 5.0.6 on 2024-07-11 13:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'permissions': [('view_reports', 'Can view agent reports'), ('manage_personnel', 'Can manage personnel'), ('sign_financial_docs', 'Can sign financial documents'), ('handle_claims', 'Can handle claims'), ('view_analytics', 'Can view analytics section'), ('view_personal_data', 'Can view personal data of employees')]},
        ),
        migrations.RemoveField(
            model_name='employee',
            name='role',
        ),
        migrations.AddField(
            model_name='employee',
            name='middle_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
