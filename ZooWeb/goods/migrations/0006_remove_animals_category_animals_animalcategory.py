# Generated by Django 5.1.3 on 2024-12-15 22:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_alter_animals_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animals',
            name='category',
        ),
        migrations.AddField(
            model_name='animals',
            name='animalcategory',
            field=models.ForeignKey(default='all', on_delete=django.db.models.deletion.CASCADE, to='goods.ticketcategories', verbose_name='Вид'),
            preserve_default=False,
        ),
    ]