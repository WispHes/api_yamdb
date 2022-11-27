from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator

from reviews.validators import validate_username


class UsersRole:
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'


ROLE = (
    (UsersRole.USER, 'Пользователь'),
    (UsersRole.MODERATOR, 'Модератор'),
    (UsersRole.ADMIN, 'Администратор'),
)


class User(AbstractUser):

    username = models.CharField(
        validators=(validate_username, UnicodeUsernameValidator),
        max_length=150,
        unique=True,
    )
    email = models.EmailField(
        max_length=254,
        unique=True,
    )
    first_name = models.CharField(
        'имя',
        max_length=150,
        blank=True
    )
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.CharField(
        'Роль',
        max_length=100,
        choices=ROLE,
        default=UsersRole.USER,
        blank=True,
    )

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.username

    @property
    def is_admin(self):
        return self.role == UsersRole.ADMIN

    @property
    def is_moderator(self):
        return self.role == UsersRole.MODERATOR

    @property
    def is_user(self):
        return self.role == UsersRole.USER
