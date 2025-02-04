# Generated by Django 4.2.2 on 2024-03-25 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_playstation4_playstation5_rename_games_playstation3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Games3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='games_images')),
            ],
        ),
        migrations.CreateModel(
            name='Games4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='games_images')),
            ],
        ),
        migrations.CreateModel(
            name='Games5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='games_images')),
            ],
        ),
        migrations.AddField(
            model_name='playstation3',
            name='game3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='games3', to='shop.games3'),
        ),
        migrations.AddField(
            model_name='playstation4',
            name='game4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='games4', to='shop.games4'),
        ),
        migrations.AddField(
            model_name='playstation5',
            name='game5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='games5', to='shop.games5'),
        ),
    ]
