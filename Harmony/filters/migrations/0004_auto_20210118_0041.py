# Generated by Django 3.1.3 on 2021-01-17 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filters', '0003_auto_20201230_2341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='region',
            name='id',
        ),
        migrations.AlterField(
            model_name='department',
            name='department_code',
            field=models.CharField(default='0', max_length=6),
        ),
    ]
