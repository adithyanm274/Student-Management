# Generated by Django 3.2.13 on 2022-10-26 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StudentApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='birth',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='product_name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='phone',
            new_name='quantity',
        ),
    ]
