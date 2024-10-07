# Generated by Django 5.1.1 on 2024-10-07 09:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MasterModels', '0052_condicioncrediticia'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImpuestoEntidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('disabled', models.BooleanField(default=False)),
                ('aplica', models.BooleanField()),
                ('porcentajexencion', models.DecimalField(decimal_places=2, max_digits=5)),
                ('resolucion', models.CharField(blank=True, max_length=100, null=True)),
                ('vigenciadesde', models.DateField()),
                ('vigenciahasta', models.DateField()),
                ('identidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MasterModels.entidad')),
                ('idimpuesto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MasterModels.impuesto')),
                ('idmodulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MasterModels.modulo')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MasterModels.persona')),
            ],
            options={
                'verbose_name': 'Impuesto por Entidad',
                'verbose_name_plural': 'ENTI - Impuestos por Entidad',
                'unique_together': {('identidad', 'idmodulo', 'idimpuesto')},
            },
        ),
    ]