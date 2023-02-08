# Generated by Django 4.1.5 on 2023-01-18 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filechecker', '0002_file_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='file',
            options={'ordering': ['status'], 'verbose_name': 'Файл', 'verbose_name_plural': 'Файлы'},
        ),
        migrations.RemoveField(
            model_name='file',
            name='is_checked',
        ),
        migrations.AddField(
            model_name='file',
            name='status',
            field=models.CharField(choices=[('new', 'new'), ('done', 'done'), ('processed', 'processed'), ('update', 'update')], default='new', max_length=100, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='logs',
            name='text',
            field=models.TextField(verbose_name='Текст'),
        ),
    ]