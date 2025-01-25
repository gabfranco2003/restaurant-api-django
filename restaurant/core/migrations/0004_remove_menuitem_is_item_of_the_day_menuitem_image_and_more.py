# Generated by Django 5.1.4 on 2025-01-25 00:36

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_menuitem_is_item_of_the_day'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='is_item_of_the_day',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='image',
            field=models.URLField(default=django.utils.timezone.now, max_length=2080),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='category',
            field=models.CharField(choices=[('Savory', 'Savory'), ('Sweet', 'Sweet'), ('Drinks', 'Drinks')], default='Savory', max_length=50),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
