# Generated by Django 2.1.5 on 2020-06-16 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20200616_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]