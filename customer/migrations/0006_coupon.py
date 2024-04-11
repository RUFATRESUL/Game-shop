# Generated by Django 4.2.2 on 2023-08-09 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_alter_wishitem_customer_basketitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=20)),
                ('discount', models.FloatField()),
                ('expire', models.DateTimeField()),
                ('limit', models.IntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('used_customers', models.ManyToManyField(related_name='used_coupons', to='customer.customer')),
            ],
        ),
    ]
