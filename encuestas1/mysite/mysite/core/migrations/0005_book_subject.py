# Generated by Django 4.1.7 on 2023-03-11 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_book_pais'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='subject',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Web Development'), (2, 'Systems Programming'), (3, 'Data Science')], null=True),
        ),
    ]
