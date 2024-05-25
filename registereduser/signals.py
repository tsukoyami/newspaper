# registereduser/signals.py
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from .models import RegisteredUser
from subscriber.models import Subscriber
from rest_framework.authtoken.models import Token


@receiver(m2m_changed, sender=RegisteredUser.company.through)
def create_subscribers(sender, instance, action, **kwargs):
    if action == 'post_add':
        for company in instance.company.all():
            Subscriber.objects.get_or_create(user=instance, company=company)

