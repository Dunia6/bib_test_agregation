# Generated by Django 4.2.3 on 2023-08-01 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='vues',
            field=models.IntegerField(default=0),
        ),
    ]
