# Generated by Django 3.2.13 on 2023-04-21 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_rename_actor_movie_actors'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='movie_id',
            new_name='movie',
        ),
    ]
