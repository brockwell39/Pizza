# Generated by Django 2.1.5 on 2020-07-03 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0018_auto_20200703_0945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='toppings',
        ),
        migrations.AddField(
            model_name='cart',
            name='toppings',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Extras'),
        ),
    ]
