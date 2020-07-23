# Generated by Django 2.1.5 on 2020-06-23 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20200616_0900'),
    ]

    operations = [
        migrations.CreateModel(
            name='Extras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topping', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.RenameField(
            model_name='fooditem',
            old_name='toppings',
            new_name='numberoftoppings',
        ),
        migrations.AddField(
            model_name='extras',
            name='canbeon',
            field=models.ManyToManyField(related_name='goeson', to='orders.Fooditem'),
        ),
    ]
