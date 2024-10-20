# Generated by Django 5.1.1 on 2024-10-20 11:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_serial_numbers_alter_info_modules_info_ec_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info_modules',
            name='info_ec_number',
            field=models.CharField(default='еЦ .   .   ', max_length=100, unique=True, verbose_name='Номер еЦ'),
        ),
        migrations.AlterField(
            model_name='reg',
            name='ec_number',
            field=models.ForeignKey(db_column='ec_number', on_delete=django.db.models.deletion.CASCADE, related_name='regs', to='main.info_modules', to_field='info_ec_number', verbose_name='Номер еЦ'),
        ),
    ]