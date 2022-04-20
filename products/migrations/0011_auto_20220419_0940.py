# Generated by Django 3.2 on 2022-04-19 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0003_maker'),
        ('products', '0010_product_maker1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='colour4',
        ),
        migrations.RemoveField(
            model_name='product',
            name='maker1',
        ),
        migrations.RemoveField(
            model_name='product',
            name='multibuy_details',
        ),
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size_selection',
        ),
        migrations.AlterField(
            model_name='product',
            name='maker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='map.maker'),
        ),
    ]