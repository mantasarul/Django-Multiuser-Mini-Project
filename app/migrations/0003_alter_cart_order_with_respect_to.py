# Generated by Django 3.2.5 on 2021-07-30 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_cart_order_with_respect_to'),
    ]

    operations = [
        migrations.AlterOrderWithRespectTo(
            name='cart',
            order_with_respect_to=None,
        ),
    ]
