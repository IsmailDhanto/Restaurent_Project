# Generated by Django 4.1.5 on 2023-01-07 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurent', '0002_rename_is_adnin_user_is_admin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='product_id',
            new_name='product',
        ),
    ]