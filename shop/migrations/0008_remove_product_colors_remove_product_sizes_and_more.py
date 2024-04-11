# Generated by Django 4.2.2 on 2024-03-11 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0011_remove_basketitem_color_remove_basketitem_size'),
        ('shop', '0007_rename_update_product_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='colors',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sizes',
        ),
        migrations.DeleteModel(
            name='Color',
        ),
        migrations.DeleteModel(
            name='Size',
        ),
    ]
