# Generated by Django 4.2.2 on 2024-04-02 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0027_alter_cargamesps3_ps3_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games3',
            name='car_games3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.cargamesps3'),
        ),
        migrations.AlterField(
            model_name='games3',
            name='child_games3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.childgamesps3'),
        ),
        migrations.AlterField(
            model_name='games3',
            name='sport_games3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.sportgamesps3'),
        ),
        migrations.AlterField(
            model_name='games3',
            name='war_games3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.wargamesps3'),
        ),
        migrations.AlterField(
            model_name='games4',
            name='car_games4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.cargamesps4'),
        ),
        migrations.AlterField(
            model_name='games4',
            name='child_games4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.childgamesps4'),
        ),
        migrations.AlterField(
            model_name='games4',
            name='sport_games4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.sportgamesps4'),
        ),
        migrations.AlterField(
            model_name='games4',
            name='war_games4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.wargamesps4'),
        ),
        migrations.AlterField(
            model_name='games5',
            name='car_games5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.cargamesps5'),
        ),
        migrations.AlterField(
            model_name='games5',
            name='child_games5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.childgamesps5'),
        ),
        migrations.AlterField(
            model_name='games5',
            name='sport_games5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.sportgamesps5'),
        ),
        migrations.AlterField(
            model_name='games5',
            name='war_games5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.wargamesps5'),
        ),
    ]
