# Generated by Django 4.2.2 on 2023-08-09 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_coupon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='used_customers',
            field=models.ManyToManyField(blank=True, related_name='used_coupons', to='customer.customer'),
        ),
    ]
