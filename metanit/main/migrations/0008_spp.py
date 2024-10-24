# Generated by Django 5.1.1 on 2024-10-14 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_info_modules_info_product_family_code_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SPP',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateField(verbose_name='Дата прохождения СПП')),
                ('user_id', models.PositiveIntegerField(verbose_name='id пользователя')),
                ('data', models.TextField(max_length=1000000, verbose_name='Текст лога с ошибков')),
                ('file', models.TextField(max_length=1000000, verbose_name='Файл')),
            ],
        ),
    ]
