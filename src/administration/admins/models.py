from django.db import models

from src.accounts.models import User


class Package(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    tokens = models.PositiveIntegerField()

    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

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

