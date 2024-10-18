from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in

class User(AbstractUser):
    ip_address = models.GenericIPAddressField(verbose_name=("IP Address"), protocol="both", unpack_ipv4=False, null=True)
    longitude = models.DecimalField(decimal_places=6, max_digits=9, null=True)
    latitude = models.DecimalField(decimal_places=6, max_digits=9, null=True)

    def __str__(self):
        return self.username

class UserSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.CharField(max_length=255)

    def __str__(self):
        return f"Session for {self.user.username}"

@receiver(user_logged_in)
def create_user_session(sender, request, user, **kwargs):
    session_key = request.session.session_key
    UserSession.objects.create(user=user, session=session_key)