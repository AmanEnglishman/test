from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, username, telegram_chat_id, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(username=username, telegram_chat_id=telegram_chat_id, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, telegram_chat_id, email, password=None):
        user = self.create_user(username, telegram_chat_id, email, password)
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True)
    telegram_chat_id = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['telegram_chat_id', 'email']

    objects = CustomUserManager()
