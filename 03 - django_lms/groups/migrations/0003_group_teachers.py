# Generated by Django 3.2.9 on 2021-12-19 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
        ('groups', '0002_group_headman'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='teachers',
            field=models.ManyToManyField(related_name='groups', to='teachers.Teacher'),
        ),
    ]
