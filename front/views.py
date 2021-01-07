from bootstrap_modal_forms.generic import BSModalCreateView
from django.urls import reverse_lazy

from front.forms import FormTestOrderModalForm, FormTestResultModalForm, FormIsolationModalForm
from front.models import FormTestOrder, FormTestResult, FormIsolation


class FormTestOrderModalView(BSModalCreateView):
    template_name = 'forms/form_test_order_modal.html'
    form_class = FormTestOrderModalForm
    success_url = reverse_lazy("home")


class FormTestResultModalView(BSModalCreateView):
    template_name = 'forms/form_test_result_modal.html'
    form_class = FormTestResultModalForm
    success_url = reverse_lazy("home")


class FormIsolationModalView(BSModalCreateView):
    template_name = 'forms/form_isolation_modal.html'
    form_class = FormIsolationModalForm
    success_url = reverse_lazy("home")
