# Generated by Django 3.2 on 2022-04-19 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_product_maker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='maker',
        ),
        migrations.RemoveField(
            model_name='product',
            name='maker2',
        ),
    ]