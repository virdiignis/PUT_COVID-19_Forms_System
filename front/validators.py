from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def put_email_validator(value):
    if not value.split('@')[1].endswith('put.poznan.pl'):
        raise ValidationError(_("Use email in put.poznan.pl domain."))
