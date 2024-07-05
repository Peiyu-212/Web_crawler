# Generated by Django 5.0.6 on 2024-07-04 07:21

import django.db.models.functions.datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('news_time', models.DateTimeField()),
                ('authority', models.CharField(max_length=200)),
                ('created_time', models.DateTimeField(db_default=django.db.models.functions.datetime.Now())),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
    ]