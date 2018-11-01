# Generated by Django 2.0.8 on 2018-10-31 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasources', '0009_unset_url_required'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasource',
            name='auth_method',
            field=models.IntegerField(choices=[('NONE', -1), ('UNKNOWN', 0), ('BASIC', 1), ('HEADER', 2)], default=0, editable=False),
        ),
    ]