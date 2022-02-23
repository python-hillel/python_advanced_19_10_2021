import datetime
import random

from core.models import Person

from django.db import models

from groups.models import Group


class Students(Person):
    phone_number = models.CharField(
        max_length=30,
        null=True,
    )

    enroll_date = models.DateField(default=datetime.date.today)
    graduate_date = models.DateField(default=datetime.date.today)
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        null=True,
        related_name='students'
    )

    @classmethod
    def _generate(cls):
        student = super()._generate()
        student.phone_number = random.randint(1000000, 9999999)
        student.save()
