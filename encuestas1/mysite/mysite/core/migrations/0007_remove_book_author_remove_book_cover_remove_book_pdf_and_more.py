# Generated by Django 4.1.7 on 2023-03-11 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_book_pais_book_sexo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='cover',
        ),
        migrations.RemoveField(
            model_name='book',
            name='pdf',
        ),
        migrations.RemoveField(
            model_name='book',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='book',
            name='title',
        ),
        migrations.AddField(
            model_name='book',
            name='nacionalidad',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='pais',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Colombia'), (2, 'Venezuela'), (3, 'Argentina'), (4, 'Phile'), (5, 'Peru'), (6, 'Mexico'), (7, 'Brazil')], null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='sexo',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Masculino'), (2, 'Femenino')], null=True),
        ),
    ]