# Generated by Django 3.2.3 on 2021-06-01 12:03

from django.db import migrations, models
import movies.models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movie_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=255, validators=[movies.models.Movie.check_title_len], verbose_name='Tytuł'),
        ),
    ]
