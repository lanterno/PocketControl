from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from users.models import AbstractUser


@python_2_unicode_compatible
class User(AbstractUser):
    avatar = models.ImageField(_('Profile Image'),
                               upload_to='users/%Y/%m/%d', blank=True)
    full_name = models.CharField(
        _('Full name'), max_length=100, null=True, blank=True, default="")

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return self.full_name or self.email

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        ordering = ('email',)
