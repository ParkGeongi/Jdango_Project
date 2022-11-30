# Generated by Django 4.1.3 on 2022-11-30 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Showtime',
            fields=[
                ('showtime_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'movie_show_times',
            },
        ),
    ]
