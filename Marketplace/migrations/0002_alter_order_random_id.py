# Generated by Django 4.1.2 on 2022-12-08 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Marketplace", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="random_id",
            field=models.IntegerField(default=4412511),
        ),
    ]
