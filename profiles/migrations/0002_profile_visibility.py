# Generated by Django 3.2.17 on 2023-02-03 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='visibility',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], default=1),
        ),
    ]