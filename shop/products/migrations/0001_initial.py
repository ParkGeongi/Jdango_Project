# Generated by Django 4.1.3 on 2022-11-30 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('price', models.TextField()),
                ('image_url', models.TextField()),
            ],
            options={
                'db_table': 'shop_products',
            },
        ),
    ]
