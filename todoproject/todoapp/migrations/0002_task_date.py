# Generated by Django 3.2.5 on 2021-08-07 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1994-05-01'),
            preserve_default=False,
        ),
    ]