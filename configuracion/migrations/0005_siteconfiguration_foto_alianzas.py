# Generated by Django 2.1.7 on 2019-06-14 16:16

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0004_auto_20190614_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfiguration',
            name='foto_alianzas',
            field=sorl.thumbnail.fields.ImageField(blank=True, help_text='1350x230', null=True, upload_to='configuracion/'),
        ),
    ]
