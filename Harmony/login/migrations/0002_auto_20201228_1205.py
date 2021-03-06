# Generated by Django 3.1.2 on 2020-12-28 11:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('content', '0002_auto_20201228_1205'),
        ('filters', '0001_initial'),
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asso', models.ManyToManyField(to='login.Association')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filters.department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='asso',
        ),
        migrations.RemoveField(
            model_name='user',
            name='department',
        ),
        migrations.DeleteModel(
            name='Account',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
