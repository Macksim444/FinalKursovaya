# Generated by Django 5.1.3 on 2024-12-15 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_alter_products_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticketcategories',
            options={'verbose_name': 'Тип Билета', 'verbose_name_plural': 'Типы Билетов'},
        ),
    ]
