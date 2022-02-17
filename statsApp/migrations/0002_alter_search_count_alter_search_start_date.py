# Generated by Django 4.0.2 on 2022-02-17 21:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('statsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='count',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='search',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]