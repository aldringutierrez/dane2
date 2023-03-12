# Generated by Django 4.1.7 on 2023-03-11 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_book_author_remove_book_cover_remove_book_pdf_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='acompanantes',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Solo'), (2, 'Familia'), (3, 'Amigos'), (4, 'Compañeros'), (5, 'Otro')], null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='edad',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='numacompanantes',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]