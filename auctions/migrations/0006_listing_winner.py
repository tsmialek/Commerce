# Generated by Django 4.2 on 2023-06-02 20:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_user_watchlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='winner',
            field=models.ForeignKey(auto_created=None, default=None, null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='winned_bets', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
