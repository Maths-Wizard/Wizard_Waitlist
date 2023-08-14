from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,
    PermissionsMixin
)
from uuid import uuid4


# Create your models here.
class UserManager(BaseUserManager):
    def _create_user(self, email):
        """ creates and saves a User
        """
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        # user.set_password(password)
        user.save(using=self._db)
        # print(f"User ==> {user}")
        return user

    def create_user(self, email):
        """
        Create and return a `User` with an email, username and password.
        """

        return self._create_user(email)


class User(AbstractBaseUser, PermissionsMixin):
    """User Model"""
    suscriber_id = models.UUIDField(default=uuid4, editable=False)
    email = models.EmailField(max_length=255, unique=True)
    # password = models.CharField(max_length=255, null=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['suscriber_id']
    objects = UserManager()

    def __str__(self) -> str:
        return self.email
