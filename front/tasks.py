import os

from celery import shared_task
from secrets import token_hex

from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.conf import settings
from django.urls import reverse

from front.models import Form


@shared_task(bind=True)
def send_confirmation_mail(self, form_id):
    try:
        form = Form.objects.get(id=form_id)
        form.confirmation_token = token_hex(128)
        form.save()

        suffix = reverse("confirm", args=(form.confirmation_token,))
        if suffix.startswith('/pl-pl/') or suffix.startswith('/en-us/'):
            suffix = suffix[4:]

        link = "https://" + settings.ALLOWED_HOSTS[0] + '/' + suffix
        html_content = f"""Dzień dobry,<br>
<br>
Twój adres email został podany w formularzu zgłoszenia przypadku do Biura ds. COVID-19 PP.<br>
Jeśli to nie ty wypełniłeś formularz, zignoruj ten email.<br>
<br>
Aby potwierdzić swoją tożsamość i przesłać formularz do biura, kliknij w poniższy link:<br>
    <a href="{link}">Potwierdź przesłanie formularza</a><br>
<br>
Prosimy nie odpowiadać na tego emaila. Jeśli masz pytania, skontaktuj się z nami pod adresem covid19@put.poznan.pl.
<br>
Pozdrawiamy<br>
Obsada Biura ds. COVID-19<br>
<br>
/<br>
<br>
Dear,<br>
<br>
your email address was used in COVID-19 reports app form. If you haven't fill form in the app, ignore this email.<br>
To confirm your identity and send form to the office, click the link below:<br>
      <a href="{link}">Confirm form</a><br>
<br>
Please do not respond to this email. Should you have any questions, contact us on covid19@put.poznan.pl.<br>
<br>
Best regards<br>
COVID-19 Office Staff Members"""

        text_content = f"""Dzień dobry,

Twój adres email został podany w formularzu zgłoszenia przypadku do Biura ds. COVID-19 PP.
Jeśli to nie ty wypełniłeś formularz, zignoruj ten email.

Aby potwierdzić swoją tożsamość i przesłać formularz do biura, skopiuj poniższy link i wklej go do paska adresu przeglądarki:
    {link}

Prosimy nie odpowiadać na tego emaila. Jeśli masz pytania, skontaktuj się z nami pod adresem covid19@put.poznan.pl.

Pozdrawiamy
Obsada Biura ds. COVID-19

/

Dear,

your email address was used in COVID-19 reports app form. If you haven't fill form in the app, ignore this email.
To confirm your identity and send form to the office, go to the link below:
      {link}

Please do not respond to this email. Should you have any questions, contact us on covid19@put.poznan.pl.

Best regards
COVID-19 Office Staff Members"""

        email = EmailMultiAlternatives(
            "Potwierdzenie przesłania formularza do biura ds. COVID-19 / COVID-19 Office Form Confirmation",
            text_content,
            settings.DEFAULT_FROM_EMAIL,
            [form.email],
            reply_to=['noreply@put.poznan.pl'],
            alternatives=((html_content, 'text/html'),)
        )
        return email.send()

    except Exception as exc:
        raise self.retry(exc=exc, countdown=30)


@shared_task(bind=True)
def send_form_by_mail(self, form_id):
    try:
        try:
            form = Form.objects.get(id=form_id)
        except Form.DoesNotExist:
            return

        text = f"""
Title:         {form.get_title_display()}
First name:    {form.first_name}
Middle name:   {form.middle_name}
Last name:     {form.last_name}
Email:         {form.email}
Phone number:  {form.phone_number}
Role:          {form.get_role_display()}
DS:            {form.get_dorm_display()}
Unit:          {form.unit}
Health state:  {form.get_health_state_display()}
"""

        try:
            form = form.formisolation
        except Form.formisolation.RelatedObjectDoesNotExist:
            pass
        else:
            form_type = "Isolation form"
            text += f"""{form_type}
Reason:        {form.reason}
Order date:    {form.order_date}
Start date:    {form.start_date}
End date:      {form.end_date}
"""

        try:
            form = form.formtestorder
        except Form.formtestorder.RelatedObjectDoesNotExist:
            pass
        else:
            form_type = "Test order form"
            text += f"""{form_type}
Reason:        {form.reason}
Order date:    {form.order_date}
Issuer:        {form.issuer}
"""

        try:
            form = form.formtestresult
        except Form.formtestresult.RelatedObjectDoesNotExist:
            pass
        else:
            form_type = "Test result form"
            text += f"""{form_type}
Reason:        {form.reason}
Order date:    {form.order_date}
Test date:     {form.test_date}
Result date:   {form.result_date}
Test result:   {form.get_test_result_display()}
Issuer:        {form.issuer}
Isolation end: {form.isolation_end}
"""

        text += f"Remarks:\t\t{form.remarks}"

        email = EmailMessage(
            f"{form_type} no. {form.id}",
            text,
            settings.DEFAULT_FROM_EMAIL,
            settings.SEND_FORMS_TO,
        )
        if form.doc:
            email.attach_file(form.doc.path)
        email.send()

        if form.doc:
            os.remove(form.doc.path)
        form.delete()

    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)
