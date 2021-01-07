from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


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
    email = models.EmailField()
    phone_number = PhoneNumberField(null=True, blank=True, unique=True, verbose_name=_("phone number"))
    role = models.CharField(max_length=1, default="N", choices=(("S", _("Student")),
                                                                ("E", _("Employee")),
                                                                ("N", _("None"))), verbose_name=_("role"))
    dorm = models.IntegerField(default=0, choices=(
        (0, _("None")),
        (1, "DS1"),
        (2, "DS2"),
        (3, "DS3"),
        (4, "DS4"),
        (5, "DS5"),
        (6, "DS6"),
    ), verbose_name=_("dorm"))
    unit = models.CharField(max_length=512, verbose_name=_("unit"))
    doc = models.FileField(max_length=300, upload_to="docs/%Y/%m/", verbose_name=_("file"))
    health_state = models.CharField(max_length=4, default="unkn", choices=(
        ("unkn", _("Asymptomatic (no test result)")),
        ("symp", _("Symptomatic (no test result)")),
        ("asym", _("Asymptomatic (positive test result)")),
        ("sick", _("Sick (positive test result)")),
        ("heal", _("Healthy (negative test result)")),
        ("held", _("Convalescent (negative test result)")),
    ), verbose_name=_("health state"))
    remarks = models.TextField(verbose_name=_("remarks"))

    class Meta:
        abstract = True


class FormTestOrder(Form):
    order_date = models.DateField(verbose_name=_("order date"))
    reason = models.TextField(verbose_name=_("reason"))
    issuer = models.CharField(max_length=255, verbose_name=_("test order issuer"))


class FormTestResult(Form):
    order_date = models.DateField(verbose_name=_("order date"))
    test_date = models.DateField(verbose_name=_("test date"))
    result_date = models.DateField(verbose_name=_("result date"))
    reason = models.TextField(verbose_name=_("reason"))
    issuer = models.CharField(max_length=255, verbose_name=_("test order issuer"))
    test_result = models.BooleanField(verbose_name=_("test result"))
    isolation_end = models.DateField(verbose_name=_("planned isolation end date"))


class FormIsolation(Form):
    reason = models.TextField(verbose_name=_("reason"))
    order_date = models.DateField(verbose_name=_("order date"))
    start_date = models.DateField(verbose_name=_("start date"))
    end_date = models.DateField(verbose_name=_("planned end date"))
