# Generated by Django 4.1.2 on 2022-10-25 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artiste',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='lyric',
            name='song_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='song',
            name='artiste_id',
            field=models.IntegerField(),
        ),
    ]
