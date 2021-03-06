# Generated by Django 3.1.4 on 2020-12-16 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Marketplace', '0005_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('electronics', 'electronics'), ('cloth', 'cloth'), ('sport', 'sport')], max_length=200, null=True),
        ),
    ]
