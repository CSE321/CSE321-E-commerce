# Generated by Django 3.1.4 on 2021-01-06 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Marketplace', '0018_remove_checkout_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
    ]
