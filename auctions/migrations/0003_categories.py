# Generated by Django 4.2.6 on 2023-10-17 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_watchlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=25)),
                ('category_listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_listing', to='auctions.auctionlisting')),
            ],
        ),
    ]
