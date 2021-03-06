# Generated by Django 2.1.5 on 2020-06-15 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catergory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catergory', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Fooditem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=64)),
                ('toppings', models.PositiveSmallIntegerField(default=0)),
                ('onesize', models.BooleanField(default=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('pricelarge', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='catergories', to='orders.Catergory')),
            ],
        ),
    ]
