# Generated by Django 4.1.6 on 2023-02-12 15:24

from django.db import migrations, models
import django.db.models.deletion
import library.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_remove_profile_genres_alter_profile_medium'),
        ('library', '0005_auto_20230207_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='profiles',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='profiles.profile'),
        ),
        migrations.AlterField(
            model_name='book',
            name='series_links',
            field=models.ManyToManyField(blank=library.models.blank_true_false, to='library.book'),
        ),
    ]