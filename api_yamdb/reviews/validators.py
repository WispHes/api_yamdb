from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_username(value):
    if value.lower() == 'me':
        raise ValidationError(
            ('Использовать имя "me" в качестве username запрещено.'),
            params={'value': value},
        )


def validate_year(value):
    if value > timezone.now().year:
        raise ValidationError(
            ('Год %(value)s больше текущего!'),
            params={'value': value},
        )
