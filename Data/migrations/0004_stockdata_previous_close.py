# Generated by Django 4.2.7 on 2023-12-19 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data', '0003_stockdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockdata',
            name='previous_close',
            field=models.FloatField(default=0),
        ),
    ]