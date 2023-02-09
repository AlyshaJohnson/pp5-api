# Generated by Django 3.2.17 on 2023-02-07 21:49

from django.db import migrations, models
import library.models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_books_series_links'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='series_book_no',
            field=models.IntegerField(blank=library.models.blank_true_false, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='series_links',
            field=models.ManyToManyField(blank=library.models.blank_true_false, related_name='_library_books_series_links_+', to='library.Books'),
        ),
    ]