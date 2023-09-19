# Generated by Django 3.2.4 on 2023-09-19 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_interaccioncliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('idActividades', models.IntegerField(db_column='idActividades', primary_key=True, serialize=False)),
                ('Fecha', models.DateField(db_column='Fecha')),
                ('FKActividades_Compra', models.ForeignKey(db_column='Actividades_Compra', on_delete=django.db.models.deletion.CASCADE, to='api.actividades_compra')),
                ('FKEstado', models.ForeignKey(db_column='FKEstado', on_delete=django.db.models.deletion.CASCADE, to='api.estado')),
                ('FKclientes', models.ForeignKey(db_column='FKclientes', on_delete=django.db.models.deletion.CASCADE, to='api.clientes')),
            ],
            options={
                'db_table': 'Compra',
            },
        ),
    ]
