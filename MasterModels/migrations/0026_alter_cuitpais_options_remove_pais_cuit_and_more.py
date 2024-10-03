# Generated by Django 5.1.1 on 2024-10-03 22:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MasterModels', '0025_cuitpais'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cuitpais',
            options={'verbose_name': 'CUIT Pais', 'verbose_name_plural': 'Paises CUIT'},
        ),
        migrations.RemoveField(
            model_name='pais',
            name='cuit',
        ),
        migrations.AlterField(
            model_name='cuitpais',
            name='idmascara',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MasterModels.mascara'),
        ),
    ]
