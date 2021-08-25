from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _

from accounts.managers import UserManager


class User(AbstractUser):
    username_validator = UnicodeUsernameValidator
    username = models.CharField(
        _('Username'),
        max_length=150,
        blank=True,
        null=True,
        unique=False,
        help_text=_(
            'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )

    # information`s
    email = models.EmailField(_('Email address'), unique=True)
    first_name = models.CharField(_("First Name"), max_length=50)
    last_name = models.CharField(_("Last Name"), max_length=50)
    profile_image = models.ImageField(_('Profil Image'), upload_to='profile_picture/', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    @property
    def profile_picture(self):
        if self.profile_image:
            return self.profile_image
        else:
            return 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ9EXGE4pl-nm5WuxE6YJT2B3wFodTHkDD8dg&usqp=CAU'

    def __str__(self):
        return self.email
