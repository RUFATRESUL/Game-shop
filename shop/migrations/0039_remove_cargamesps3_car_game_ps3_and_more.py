# Generated by Django 4.2.2 on 2024-04-07 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0038_remove_games3_car_games3_remove_games3_child_games3_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cargamesps3',
            name='car_game_ps3',
        ),
        migrations.RemoveField(
            model_name='cargamesps4',
            name='car_game_ps4',
        ),
        migrations.RemoveField(
            model_name='cargamesps5',
            name='car_game_ps5',
        ),
        migrations.RemoveField(
            model_name='childgamesps3',
            name='child_game_ps3',
        ),
        migrations.RemoveField(
            model_name='childgamesps4',
            name='child_game_ps4',
        ),
        migrations.RemoveField(
            model_name='childgamesps5',
            name='child_game_ps5',
        ),
        migrations.RemoveField(
            model_name='sportgamesps3',
            name='sport_game_ps3',
        ),
        migrations.RemoveField(
            model_name='sportgamesps4',
            name='sport_game_ps4',
        ),
        migrations.RemoveField(
            model_name='sportgamesps5',
            name='sport_game_ps5',
        ),
        migrations.RemoveField(
            model_name='wargamesps3',
            name='war_game_ps3',
        ),
        migrations.RemoveField(
            model_name='wargamesps4',
            name='war_game_ps4',
        ),
        migrations.RemoveField(
            model_name='wargamesps5',
            name='war_game_ps5',
        ),
        migrations.AddField(
            model_name='cargamesps3',
            name='car_game_ps3',
            field=models.ManyToManyField(to='shop.games3'),
        ),
        migrations.AddField(
            model_name='cargamesps4',
            name='car_game_ps4',
            field=models.ManyToManyField(to='shop.games4'),
        ),
        migrations.AddField(
            model_name='cargamesps5',
            name='car_game_ps5',
            field=models.ManyToManyField(to='shop.games5'),
        ),
        migrations.AddField(
            model_name='childgamesps3',
            name='child_game_ps3',
            field=models.ManyToManyField(to='shop.games3'),
        ),
        migrations.AddField(
            model_name='childgamesps4',
            name='child_game_ps4',
            field=models.ManyToManyField(to='shop.games4'),
        ),
        migrations.AddField(
            model_name='childgamesps5',
            name='child_game_ps5',
            field=models.ManyToManyField(to='shop.games5'),
        ),
        migrations.AddField(
            model_name='sportgamesps3',
            name='sport_game_ps3',
            field=models.ManyToManyField(to='shop.games3'),
        ),
        migrations.AddField(
            model_name='sportgamesps4',
            name='sport_game_ps4',
            field=models.ManyToManyField(to='shop.games4'),
        ),
        migrations.AddField(
            model_name='sportgamesps5',
            name='sport_game_ps5',
            field=models.ManyToManyField(to='shop.games5'),
        ),
        migrations.AddField(
            model_name='wargamesps3',
            name='war_game_ps3',
            field=models.ManyToManyField(to='shop.games3'),
        ),
        migrations.AddField(
            model_name='wargamesps4',
            name='war_game_ps4',
            field=models.ManyToManyField(to='shop.games4'),
        ),
        migrations.AddField(
            model_name='wargamesps5',
            name='war_game_ps5',
            field=models.ManyToManyField(to='shop.games5'),
        ),
    ]
