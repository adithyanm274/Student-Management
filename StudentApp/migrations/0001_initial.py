# Generated by Django 3.2.13 on 2022-10-26 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birth', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to='image/')),
            ],
        ),
    ]