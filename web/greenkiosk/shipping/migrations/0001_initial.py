# Generated by Django 3.1.2 on 2020-10-01 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DispenserCoolerBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=6)),
                ('unlock_field', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ShippingProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=6)),
                ('date_joined', models.CharField(max_length=6)),
                ('email', models.EmailField(max_length=50)),
                ('phone_number', models.IntegerField()),
                ('transport_mode', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dispatch_time', models.DateTimeField()),
                ('cooler_box', models.CharField(blank=True, max_length=20, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.order')),
                ('shipping_provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shipping.shippingprovider')),
            ],
        ),
    ]
