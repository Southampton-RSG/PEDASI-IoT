# Generated by Django 2.0.8 on 2018-12-19 11:58

import datasources.connectors.base
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasources', '0018_editable_auth_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasource',
            name='auth_method',
            field=models.IntegerField(choices=[(-1, 'NONE'), (0, 'UNKNOWN'), (1, 'BASIC'), (2, 'HEADER')], default=datasources.connectors.base.AuthMethod(0)),
        ),
    ]