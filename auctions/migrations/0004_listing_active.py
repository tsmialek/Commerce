# Generated by Django 4.2 on 2023-05-31 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_alter_listing_end_time_alter_listing_time_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='active',
            field=models.BooleanField(auto_created=True, default=True),
            preserve_default=False,
        ),
    ]
