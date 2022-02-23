import random

from core.models import Person

from django.db import models


class Teacher(Person):
    salary = models.PositiveIntegerField(default=1500)

    @classmethod
    def _generate(cls):
        teacher = super()._generate()
        teacher.salary = random.randint(10000, 99999)
        teacher.save()
