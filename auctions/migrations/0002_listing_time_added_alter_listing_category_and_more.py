# Generated by Django 4.2 on 2023-05-31 11:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='time_added',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 31, 11, 45, 38, 706662, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('electronics', 'Electronics'), ('fashion', 'Fashion'), ('sport', 'Sport'), ('home', 'Home'), ('health', 'Health'), ('other', 'Other')], max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='end_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
