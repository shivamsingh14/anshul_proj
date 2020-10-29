from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.core import validators
from django.utils.translation import gettext_lazy as _

class RegexaValidator(validators.RegexValidator):

    regex = r'^[\w.@+-+;]+$'

class MNS(AbstractUser):

    username_validator = RegexaValidator()
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )

 