# Generated by Django 4.2.2 on 2024-03-31 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0023_games3_ps3_category_games3_ps4_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games3',
            name='ps3_category',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ps3_category_game3', to='shop.playstation3'),
        ),
        migrations.AlterField(
            model_name='games3',
            name='ps4_category',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ps3_category_game4', to='shop.playstation4'),
        ),
        migrations.AlterField(
            model_name='games3',
            name='ps5_category',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ps3_category_game5', to='shop.playstation5'),
        ),
        migrations.AlterField(
            model_name='games4',
            name='ps3_category',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ps4_category_game3', to='shop.playstation3'),
        ),
        migrations.AlterField(
            model_name='games4',
            name='ps4_category',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ps4_category_game4', to='shop.playstation4'),
        ),
        migrations.AlterField(
            model_name='games4',
            name='ps5_category',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ps4_category_game5', to='shop.playstation5'),
        ),
        migrations.AlterField(
            model_name='games5',
            name='ps3_category',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ps5_category_game3', to='shop.playstation3'),
        ),
        migrations.AlterField(
            model_name='games5',
            name='ps4_category',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ps5_category_game4', to='shop.playstation4'),
        ),
        migrations.AlterField(
            model_name='games5',
            name='ps5_category',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ps5_category_game5', to='shop.playstation5'),
        ),
    ]
