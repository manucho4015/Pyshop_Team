# Generated by Django 3.0.5 on 2020-06-03 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20200603_1236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='active',
        ),
        migrations.RemoveField(
            model_name='product',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='product',
            name='updated',
        ),
    ]