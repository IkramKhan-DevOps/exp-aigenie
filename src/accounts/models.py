from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_resized import ResizedImageField

"""
At the start please be careful to start migrations
--------------------------------------------------

STEP: 1 comment current_subscription [FIELD] in model [USER]
STEP: 1 py manage.py makemigrations accounts
STEP: 2 py manage.py migrate
Then do next ...

"""


class User(AbstractUser):
    profile_image = ResizedImageField(
        upload_to='accounts/images/profiles/', null=True, blank=True, size=[250, 250], quality=75, force_format='PNG',
        help_text='size of logo must be 250*250 and format must be png image file', crop=['middle', 'center']
    )
    phone_number = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username

    def delete(self, *args, **kwargs):
        self.profile_image.delete(save=True)
        super(User, self).delete(*args, **kwargs)

    def get_user_name(self):
        if self.first_name or self.last_name:
            return self.first_name + " " + self.last_name
        return self.username

    def get_user_profile(self):
        profile, flag = Profile.objects.get_or_create(user=self)
        return profile


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)

    tokens_total = models.PositiveIntegerField(default=0)
    tokens_used = models.PositiveIntegerField(default=0)
    tokens_available = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.get_user_name()


@receiver(post_save, sender=settings.AUTH_USER_MODEL, dispatch_uid="user_registered")
def on_user_registration(sender, instance, created, **kwargs):
    """
    :TOPIC if user creates at any point the statistics model will be initialized
    :param sender:
    :param instance:
    :param created:
    :param kwargs:
    :return:
    """
    if created:
        profile = instance.get_user_profile()
