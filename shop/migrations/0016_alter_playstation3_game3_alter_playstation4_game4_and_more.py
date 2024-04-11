# Generated by Django 4.2.2 on 2024-03-25 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_remove_playstation3_game3_remove_playstation4_game4_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playstation3',
            name='game3',
            field=models.ManyToManyField(related_name='games3', to='shop.games3'),
        ),
        migrations.AlterField(
            model_name='playstation4',
            name='game4',
            field=models.ManyToManyField(related_name='games4', to='shop.games4'),
        ),
        migrations.AlterField(
            model_name='playstation5',
            name='game5',
            field=models.ManyToManyField(related_name='games5', to='shop.games5'),
        ),
    ]
