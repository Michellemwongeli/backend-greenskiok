# Generated by Django 3.1.2 on 2020-10-01 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField()),
                ('total_price', models.DecimalField(decimal_places=5, max_digits=6)),
                ('status', models.CharField(max_length=60)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.product')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(max_length=60)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=30)),
                ('date_Of_Payment', models.DateTimeField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.IntegerField()),
                ('date_placed', models.DateTimeField()),
                ('status', models.CharField(max_length=100)),
                ('delivery_time', models.DateTimeField()),
                ('order_price', models.DecimalField(decimal_places=3, max_digits=30)),
                ('shipping_cost', models.DecimalField(decimal_places=4, max_digits=40)),
                ('total_price', models.DecimalField(decimal_places=5, max_digits=20)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.cart')),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
            ],
        ),
    ]
