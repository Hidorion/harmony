# Generated by Django 3.1.3 on 2021-01-24 14:57

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('content', '0007_auto_20210115_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='approved',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='image',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='image',
            name='posting_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
