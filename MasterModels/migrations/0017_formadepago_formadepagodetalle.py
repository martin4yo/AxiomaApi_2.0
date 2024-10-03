# Generated by Django 5.1.1 on 2024-10-03 19:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MasterModels', '0016_remove_tipodocumento_mascara_tipodocumento_idmascara'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormaDePago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('disabled', models.BooleanField(default=False)),
                ('nombre', models.CharField(max_length=100)),
                ('codigo', models.CharField(default='', max_length=10)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MasterModels.persona')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FormaDePagoDetalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('disabled', models.BooleanField(default=False)),
                ('dias', models.IntegerField()),
                ('porcentaje', models.DecimalField(decimal_places=2, max_digits=5)),
                ('idformadepago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MasterModels.formadepago')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MasterModels.persona')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
