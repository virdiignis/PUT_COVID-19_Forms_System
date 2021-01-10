from bootstrap_modal_forms.generic import BSModalCreateView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from front.forms import FormTestOrderModalForm, FormTestResultModalForm, FormIsolationModalForm
from front.models import Form
from front.tasks import send_confirmation_mail, send_form_by_mail


def home(request):
    return render(request, "home.html")


def email(request):
    return render(request, "email.html")


def confirm(request, token):
    try:
        f = Form.objects.get(confirmation_token=token)
        send_form_by_mail.delay(f.id)
    except Form.DoesNotExist:
        pass

    return render(request, "confirm.html")


class FormTestOrderModalView(BSModalCreateView):
    template_name = 'forms/form_test_order_modal.html'
    form_class = FormTestOrderModalForm
    success_url = reverse_lazy("email")

    def form_valid(self, form):
        super(FormTestOrderModalView, self).form_valid(form)
        if not self.request.is_ajax() or self.request.POST.get('asyncUpdate') == 'True':
            send_confirmation_mail.delay(self.object.id)
            return redirect(self.get_success_url())
        else:
            return HttpResponse()


class FormTestResultModalView(BSModalCreateView):
    template_name = 'forms/form_test_result_modal.html'
    form_class = FormTestResultModalForm
    success_url = reverse_lazy("email")

    def form_valid(self, form):
        super(FormTestResultModalView, self).form_valid(form)
        if not self.request.is_ajax() or self.request.POST.get('asyncUpdate') == 'True':
            send_confirmation_mail.delay(self.object.id)
            return redirect(self.get_success_url())
        else:
            return HttpResponse()


class FormIsolationModalView(BSModalCreateView):
    template_name = 'forms/form_isolation_modal.html'
    form_class = FormIsolationModalForm
    success_url = reverse_lazy("email")

    def form_valid(self, form):
        super(FormIsolationModalView, self).form_valid(form)
        if not self.request.is_ajax() or self.request.POST.get('asyncUpdate') == 'True':
            send_confirmation_mail.delay(self.object.id)
            return redirect(self.get_success_url())
        else:
            return HttpResponse()
