# Generated by Django 5.0 on 2023-12-18 12:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='todolist',
            name='category',
            field=models.ForeignKey(default='general', on_delete=django.db.models.deletion.PROTECT, to='todolist.category'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='created',
            field=models.DateField(default='2023-12-18'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='due_date',
            field=models.DateField(default='2023-12-18'),
        ),
    ]
