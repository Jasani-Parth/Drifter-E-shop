# Generated by Django 3.2.7 on 2021-10-04 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_product_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=2),
        ),
    ]
