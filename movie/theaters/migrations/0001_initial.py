# Generated by Django 4.1.3 on 2022-11-30 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movie_theater',
            fields=[
                ('theater_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('seat', models.IntegerField()),
            ],
            options={
                'db_table': 'movie_theaters',
            },
        ),
    ]
