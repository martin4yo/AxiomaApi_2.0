# Generated by Django 5.1.1 on 2024-10-04 17:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MasterModels', '0036_alter_indice_unique_together_indice_importe_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipoindice',
            name='idtipofrecuencia',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='MasterModels.tipofrecuencia'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tipoindice',
            name='idtipovalor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='MasterModels.tipovalor'),
            preserve_default=False,
        ),
    ]
