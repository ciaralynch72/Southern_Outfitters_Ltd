# Generated by Django 3.2 on 2023-05-20 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_alter_order_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(max_length=40),
        ),
    ]
