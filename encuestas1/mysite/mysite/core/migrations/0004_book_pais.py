# Generated by Django 4.1.7 on 2023-03-11 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_book_pais'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pais',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]