# Generated by Django 4.1.3 on 2022-11-30 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('ocreated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'shop_orders',
            },
        ),
    ]
