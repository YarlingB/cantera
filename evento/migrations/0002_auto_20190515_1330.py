# Generated by Django 2.1.7 on 2019-05-15 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evento',
            old_name='title',
            new_name='tittle',
        ),
    ]
