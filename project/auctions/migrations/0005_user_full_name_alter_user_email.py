# Generated by Django 4.2.7 on 2023-12-16 15:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0004_remove_listing_starting_bid_listing_watchlist_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="full_name",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
