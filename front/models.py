from django.core.validators import EmailValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

from front.validators import put_email_validator


class Form(models.Model):
    title = models.CharField(max_length=4, default="Mr", choices=(
        ("Mr", _("Mr")),
        ("Ms", _("Ms")),
        ("inz", _("eng.")),
        ("mgr", _("msc")),
        ("mgri", _("msc eng.")),
        ("dr", _("dr")),
        ("dri", _("dr eng.")),
        ("drh", _("dr habil.")),
        ("drhi", _("dr habil. eng.")),
        ("prh", _("prof. dr habil.")),
        ("prhi", _("prof. dr habil. eng.")),
        ("prp", _("dr habil. prof. PUT")),
        ("prip", _("dr habil. eng. prof. PUT")),
    ), verbose_name=_("title"))
    first_name = models.CharField(max_length=32, verbose_name=_("first name"))
    middle_name = models.CharField(max_length=32, null=True, blank=True, verbose_name=_("middle name"))
    last_name = models.CharField(max_length=32, verbose_name=_("last name"))
    email = models.EmailField(validators=[EmailValidator, put_email_validator],
                              help_text=_("Use your PUT email, so we can verify your identity."))
    phone_number = PhoneNumberField(null=True, blank=True, verbose_name=_("phone number"),
                                    help_text=_("Phone number needs to start with area code e.g. +48 for Poland."))
    role = models.CharField(max_length=1, default="E", choices=(("S", _("Student")),
                                                                ("E", _("Employee")),
                                                                ("N", _("None"))), verbose_name=_("role"),
                            help_text=_("PhD students are supposed to select 'Student'."))
    dorm = models.IntegerField(default=0, choices=(
        (0, _("None")),
        (1, "DS1"),
        (2, "DS2"),
        (3, "DS3"),
        (4, "DS4"),
        (5, "DS5"),
        (6, "DS6"),
    ), verbose_name=_("dorm"), help_text=_("Only choose dorm if you currently live in one."))
    unit = models.CharField(max_length=512, verbose_name=_("unit"),
                            help_text=_("Faculty in case of students, Institute in case of employees."))
    health_state = models.CharField(max_length=4, default="unkn", choices=(
        ("unkn", _("Asymptomatic (no test result)")),
        ("symp", _("Symptomatic (no test result)")),
        ("asym", _("Asymptomatic (positive test result)")),
        ("sick", _("Sick (positive test result)")),
        ("heal", _("Healthy (negative test result)")),
        ("held", _("Convalescent (negative test result)")),
    ), verbose_name=_("current health state"))

    isolation_place = models.CharField(max_length=1, default='H', choices=(
        ("H", _("Home")),
        ("S", _("Hospital")),
        ("D", _("DS4")),
        ("I", _("Isolation ward"))), verbose_name=_("isolation place"))

    doc = models.FileField(max_length=300, upload_to="docs/%Y/%m/", verbose_name=_("Confirmation document"), null=True,
                           blank=True, help_text=_("Here you can upload PDF document confirming sent data. (optional)"))
    remarks = models.TextField(verbose_name=_("remarks"), null=True, blank=True,
                               help_text=_("Tell us if this form missed anything important."))

    confirmation_token = models.CharField(max_length=256, null=True, editable=False, unique=True)


class FormTestOrder(Form):
    order_date = models.DateField(verbose_name=_("test order date"))
    reason = models.TextField(verbose_name=_("reason to get tested"),
                              help_text=_("e.g. symptoms, had contact with sick person etc."))
    issuer = models.CharField(max_length=255, verbose_name=_("test order issuer"),
                              help_text=_("e.g. doctor, SANEPID, private"))


class FormTestResult(Form):
    order_date = models.DateField(verbose_name=_("test order date"))
    test_date = models.DateField(verbose_name=_("test date"))
    result_date = models.DateField(verbose_name=_("result date"))
    test_result = models.BooleanField(verbose_name=_("test result"),
                                      choices=((True, _('Positive')), (False, _('Negative'))))
    reason = models.TextField(verbose_name=_("reason to get tested"),
                              help_text=_("e.g. symptoms, had contact with sick person etc."))
    issuer = models.CharField(max_length=255, verbose_name=_("test order issuer"),
                              help_text=_("e.g. doctor, SANEPID, private"))
    isolation_end = models.DateField(verbose_name=_("planned isolation end date"))


class FormIsolation(Form):
    reason = models.TextField(verbose_name=_("isolation reason"),
                              help_text=_(
                                  "If your isolation is caused by test order or positive test result, use the respective forms to report it."))
    order_date = models.DateField(verbose_name=_("order date"))
    start_date = models.DateField(verbose_name=_("start date"))
    end_date = models.DateField(verbose_name=_("planned end date"))
