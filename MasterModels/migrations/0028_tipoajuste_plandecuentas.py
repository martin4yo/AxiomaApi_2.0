# Generated by Django 5.1.1 on 2024-10-04 10:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MasterModels', '0027_tipoindice'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoAjuste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('disabled', models.BooleanField(default=False)),
                ('nombre', models.CharField(max_length=100)),
                ('codigo', models.CharField(default='', max_length=1, unique=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MasterModels.persona')),
            ],
            options={
                'verbose_name': 'Tipo de Ajuste',
                'verbose_name_plural': 'Tipos de Ajuste Contable',
            },
        ),
        migrations.CreateModel(
            name='PlanDeCuentas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('disabled', models.BooleanField(default=False)),
                ('nombre', models.CharField(max_length=256)),
                ('codigo', models.CharField(max_length=20, unique=True)),
                ('imputable', models.BooleanField(default=False)),
                ('bimonetaria', models.BooleanField(default=False)),
                ('nivel', models.IntegerField()),
                ('idpadre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MasterModels.plandecuentas')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MasterModels.persona')),
                ('ajustable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MasterModels.tipoajuste')),
            ],
            options={
                'verbose_name': 'Cuenta Contable',
                'verbose_name_plural': 'Plan de Cuentas',
                'unique_together': {('codigo',)},
            },
        ),
    ]
