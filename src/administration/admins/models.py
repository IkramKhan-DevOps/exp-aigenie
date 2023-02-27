from django.db import models

from src.accounts.models import User


class Package(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    tokens = models.PositiveIntegerField()
    priority = models.PositiveIntegerField(default=0)

    is_popular = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['priority']

    def __str__(self):
        return self.name


class Purchase(models.Model):
    PAYMENT_METHOD_TYPES = (
        ('gp', 'Google Pay'),
        ('ap', 'Apple Pay'),
    )
    user = models.ForeignKey(User, related_name='users', on_delete=models.SET_NULL, null=True, blank=False)
    package = models.ForeignKey(Package, related_name='packages', on_delete=models.SET_NULL, null=True, blank=False)
    amount_total = models.FloatField()
    amount_paid = models.FloatField()
    tokens = models.PositiveIntegerField()
    payment_method = models.CharField(max_length=2, default='gp', choices=PAYMENT_METHOD_TYPES)

    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on', 'package']

    def __str__(self):
        return str(self.pk)


class ApplicationSoftware(models.Model):

    name = models.CharField(max_length=255)
    version = models.FloatField(help_text="Application version must be update [0.*] or upgrade [*.0]")
    description = models.TextField(null=True, blank=True, help_text="Detailed down description")
    app_file = models.FileField(upload_to='applications/', help_text="Please user a installers or zip files here")
    android_link = models.URLField(null=True, blank=True)
    ios_link = models.URLField(null=True, blank=True)

    total_downloads = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Applications and Versions"

    def __str__(self):
        return self.name
