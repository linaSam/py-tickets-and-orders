# Generated by Django 4.0.2 on 2022-10-28 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0004_alter_movie_actors_alter_movie_genres_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='movie_session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.moviesession'),
        ),
    ]