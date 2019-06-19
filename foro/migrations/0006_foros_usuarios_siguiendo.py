# Generated by Django 2.1.7 on 2019-06-17 17:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('foro', '0005_auto_20190614_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='foros',
            name='usuarios_siguiendo',
            field=models.ManyToManyField(blank=True, editable=False, related_name='siguiendo', to=settings.AUTH_USER_MODEL),
        ),
    ]