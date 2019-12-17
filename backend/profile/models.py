from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
import random
from django.db.models.signals import pre_save


def pre_save_key_email(sender, instance, *args, **kwargs):
    chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    password = ''
    for n in range(4):
        for i in range(4):
            password += random.choice(chars)
        password += '-'
    print(password)
    instance.key = password[:-1]
    if instance.user.email:
        instance.email = instance.user.email


class LicenseBrickDesign(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name=_('User'))
    key = models.SlugField(max_length=19, blank=True, verbose_name=_('Key'))
    computer_name = models.CharField(max_length=250, blank=True, verbose_name=_('Computer name'))
    id_program = models.CharField(max_length=8, blank=True, verbose_name=_('ID program'))
    email = models.EmailField(blank=True, default='xxx@xxx.xx', verbose_name=_('E-mail'))

    class Meta:
        verbose_name = _('Licenses BrickDesigner_BD001')
        verbose_name_plural = _('Licenses BrickDesigner_BD001')

    def __str__(self):
        return self.user.email


pre_save.connect(pre_save_key_email, sender=LicenseBrickDesign)
