# Generated by Django 5.1.4 on 2025-01-25 04:34

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_menuitem_is_item_of_the_day_alter_menuitem_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='image',
            field=models.URLField(default=django.utils.timezone.now, max_length=2080),
            preserve_default=False,
        ),
    ]
