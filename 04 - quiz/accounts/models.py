from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True)
    avatar = models.ImageField(upload_to='profile/', default='default.png')
    birthday = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)

    class Meta(AbstractUser.Meta):
        permissions = [
            ('view_statistics', 'View extra data'),
        ]

    def __str__(self):
        return self.username


@receiver(post_save, sender=CustomUser)
def save_user(sender, instance, created, **kwargs):
    if created:
        instance.groups.add(Group.objects.get(name='Users'))
