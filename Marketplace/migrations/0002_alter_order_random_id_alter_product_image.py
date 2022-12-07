# Generated by Django 4.1.2 on 2022-12-07 18:04

import Marketplace.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Marketplace', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='random_id',
            field=models.IntegerField(default=3347688),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.URLField(validators=[django.core.validators.URLValidator(), Marketplace.models.validate_image_quality]),
        ),
    ]
