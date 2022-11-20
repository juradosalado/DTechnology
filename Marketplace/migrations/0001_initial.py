# Generated by Django 4.1.1 on 2022-11-20 10:58

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('surname', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None, unique=True)),
                ('street_address', models.CharField(max_length=100)),
                ('apartment_address', models.CharField(max_length=100)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('address_type', models.CharField(choices=[('B', 'Billing'), ('S', 'Shipping')], max_length=1)),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('purcharse_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('discount_price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('section', models.CharField(choices=[('MB', 'Motherboard'), ('CPU', 'Processor'), ('HDD', 'Hard Disk Drive'), ('SSD', 'Solid State Drive'), ('GPU', 'Graphic Card'), ('RAM', 'Ram Memory'), ('RC', 'DVD/CD Recorder'), ('SC', 'Sound Card'), ('CC', 'Computer Cases'), ('V', 'Ventilation'), ('PS', 'Power Supply'), ('MS', 'Mouses'), ('KB', 'Keyboards'), ('SP', 'Speakers'), ('HP', 'Headphones'), ('GC', 'Gaming Chairs'), ('WC', 'Webcam'), ('PT', 'Printers'), ('GS', 'Games'), ('CS', 'Consoles'), ('CA', 'Console Accessories'), ('CT', 'Controls')], max_length=10)),
                ('description', models.TextField(max_length=400)),
                ('image', models.URLField()),
                ('department', models.CharField(choices=[('CM', 'Components'), ('PP', 'Peripherals'), ('VG', 'Consoles and Videogames')], max_length=10)),
                ('producer', models.CharField(choices=[('AS', 'Asus'), ('LV', 'Lenovo'), ('HP', 'HP'), ('SY', 'Sony'), ('XB', 'Xbox'), ('NT', 'Nintendo'), ('NS', 'New Skill'), ('MSI', 'MSI'), ('PH', 'Philips'), ('GB', 'Gigabyte'), ('EV', 'Evga'), ('NV', 'Nvidia'), ('UB', 'Ubisoft'), ('SM', 'Santa Monica'), ('IT', 'Intel'), ('AMD', 'AMD'), ('ZT', 'Zotac')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(blank=True, max_length=100, null=True)),
                ('quantity', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Marketplace.product', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('ref_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('ordered_date', models.DateTimeField()),
                ('ordered', models.BooleanField(default=False)),
                ('being_delivered', models.BooleanField(default=False)),
                ('received', models.BooleanField(default=False)),
                ('billing_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='billing_address', to='Marketplace.address')),
                ('payment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Marketplace.payment')),
                ('products', models.ManyToManyField(to='Marketplace.orderproduct')),
                ('shipping_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shipping_address', to='Marketplace.address')),
            ],
        ),
    ]
