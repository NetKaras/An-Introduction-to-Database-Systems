# Generated by Django 3.1.4 on 2020-12-24 08:55

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseList',
            fields=[
                ('purchase_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('purchase_date', models.DateField(default=datetime.date.today, validators=[django.core.validators.MaxValueValidator(datetime.date.today)])),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='category_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodapp.category'),
        ),
        migrations.CreateModel(
            name='PurchaseDetail',
            fields=[
                ('detail_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('product_cost', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodapp.product')),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodapp.purchaselist')),
            ],
        ),
    ]
