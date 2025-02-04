# Generated by Django 4.2.2 on 2024-03-31 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_remove_games3_image_remove_games3_play_station3_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cargames',
            name='car_games3',
        ),
        migrations.RemoveField(
            model_name='cargames',
            name='car_games4',
        ),
        migrations.RemoveField(
            model_name='cargames',
            name='car_games5',
        ),
        migrations.RemoveField(
            model_name='childgames',
            name='child_games3',
        ),
        migrations.RemoveField(
            model_name='childgames',
            name='child_games4',
        ),
        migrations.RemoveField(
            model_name='childgames',
            name='child_games5',
        ),
        migrations.RemoveField(
            model_name='sportgames',
            name='sport_games3',
        ),
        migrations.RemoveField(
            model_name='sportgames',
            name='sport_games4',
        ),
        migrations.RemoveField(
            model_name='sportgames',
            name='sport_games5',
        ),
        migrations.RemoveField(
            model_name='wargames',
            name='war_games3',
        ),
        migrations.RemoveField(
            model_name='wargames',
            name='war_games4',
        ),
        migrations.RemoveField(
            model_name='wargames',
            name='war_games5',
        ),
        migrations.AddField(
            model_name='games3',
            name='car_games3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_games5', to='shop.cargames'),
        ),
        migrations.AddField(
            model_name='games3',
            name='child_games3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_games3', to='shop.childgames'),
        ),
        migrations.AddField(
            model_name='games3',
            name='sport_games3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_games5', to='shop.sportgames'),
        ),
        migrations.AddField(
            model_name='games3',
            name='war_games3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_games4', to='shop.wargames'),
        ),
        migrations.AddField(
            model_name='games4',
            name='car_games4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sport_games5', to='shop.cargames'),
        ),
        migrations.AddField(
            model_name='games4',
            name='child_games4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sport_games3', to='shop.childgames'),
        ),
        migrations.AddField(
            model_name='games4',
            name='sport_games4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sport_games5', to='shop.sportgames'),
        ),
        migrations.AddField(
            model_name='games4',
            name='war_games4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sport_games4', to='shop.wargames'),
        ),
        migrations.AddField(
            model_name='games5',
            name='car_games5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='war_games5', to='shop.cargames'),
        ),
        migrations.AddField(
            model_name='games5',
            name='child_games5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='war_games3', to='shop.childgames'),
        ),
        migrations.AddField(
            model_name='games5',
            name='sport_games5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='war_games5', to='shop.sportgames'),
        ),
        migrations.AddField(
            model_name='games5',
            name='war_games5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='war_games4', to='shop.wargames'),
        ),
    ]
