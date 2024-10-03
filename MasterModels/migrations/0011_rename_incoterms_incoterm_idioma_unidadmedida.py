# Generated by Django 5.1.1 on 2024-10-03 17:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MasterModels', '0010_incoterms'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Incoterms',
            new_name='Incoterm',
        ),
        migrations.CreateModel(
            name='Idioma',
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
            name='UnidadMedida',
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
    ]
