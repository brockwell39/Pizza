# Generated by Django 2.1.5 on 2020-06-16 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5),
        ),
    ]
