# Generated by Django 2.1.5 on 2020-07-07 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0026_cart_itemid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='toppings',
            field=models.ManyToManyField(blank=True, null=True, to='orders.Top'),
        ),
    ]
