# Generated by Django 2.1.5 on 2020-07-17 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0033_auto_20200710_0935'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
