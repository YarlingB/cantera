# Generated by Django 2.1.7 on 2019-06-11 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puntosvista', '0002_puntos_fecha_creacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puntos',
            name='fecha_creacion',
            field=models.DateField(verbose_name='Fecha de publicación'),
        ),
    ]
