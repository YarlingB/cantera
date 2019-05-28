# Generated by Django 2.1.7 on 2019-05-28 16:18

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('foro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foros',
            name='foto',
            field=sorl.thumbnail.fields.ImageField(default=1, upload_to='foros/', verbose_name='Foto'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='foros',
            name='nombre',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
