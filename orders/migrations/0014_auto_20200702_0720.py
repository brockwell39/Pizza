# Generated by Django 2.1.5 on 2020-07-02 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='item',
            field=models.CharField(max_length=64),
        ),
    ]
