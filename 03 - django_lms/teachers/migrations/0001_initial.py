# Generated by Django 3.2.9 on 2021-12-19 12:17

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2)])),
                ('last_name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2)])),
                ('age', models.IntegerField()),
                ('birthday', models.DateField(default=datetime.date.today)),
                ('salary', models.PositiveIntegerField(default=1500)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
