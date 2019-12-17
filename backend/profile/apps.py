from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class AccountsApConfig(AppConfig):
    name = 'backend.profile'
    verbose_name = _('Users and licenses')
