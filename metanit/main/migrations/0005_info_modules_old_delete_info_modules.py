# Generated by Django 5.1.1 on 2024-10-08 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_info_modules_remove_reg_family_remove_reg_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='info_modules_old',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info_ec_number', models.CharField(default='Номер еЦ', max_length=100)),
                ('info_product_family', models.CharField(max_length=100, verbose_name='Семейство продукта')),
                ('info_revision', models.PositiveIntegerField(verbose_name='Ревизия')),
                ('info_product_type', models.CharField(max_length=100, verbose_name='Тип продукта')),
                ('info_manufacturer', models.CharField(max_length=100, verbose_name='Производитель')),
                ('info_manufacturer_code', models.PositiveIntegerField(verbose_name='Код производителя')),
                ('info_product_type_code', models.PositiveIntegerField(verbose_name='Код типа продукта')),
                ('info_revision_code', models.PositiveIntegerField(verbose_name='Код ревизии')),
            ],
        ),
        migrations.DeleteModel(
            name='info_modules',
        ),
    ]
