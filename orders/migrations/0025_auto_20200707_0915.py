# Generated by Django 2.1.5 on 2020-07-07 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0024_auto_20200707_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='item',
            field=models.CharField(default=2, max_length=64),
            preserve_default=False,
        ),
    ]
