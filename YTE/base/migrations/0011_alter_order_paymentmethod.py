# Generated by Django 4.0.4 on 2022-05-10 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_remove_shippingaddress_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='paymentMethod',
            field=models.CharField(blank=True, choices=[('onl', 'Online'), ('off', 'Pay when received')], max_length=200, null=True),
        ),
    ]
