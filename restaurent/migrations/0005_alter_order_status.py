# Generated by Django 4.1.5 on 2023-01-08 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurent', '0004_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, default='process', max_length=20, null=True),
        ),
    ]
