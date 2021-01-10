from bootstrap_modal_forms.forms import BSModalModelForm
from django.forms import DateInput, FileInput

from front.models import FormTestOrder, FormTestResult, FormIsolation


class FormTestOrderModalForm(BSModalModelForm):
    class Meta:
        model = FormTestOrder
        fields = "__all__"
        widgets = {
            "order_date": DateInput(format='%d.%m.%Y', attrs={'class': 'form-control datefield'}),
            "doc": FileInput(attrs={'accept': 'application/pdf'}),
        }


class FormTestResultModalForm(BSModalModelForm):
    class Meta:
        model = FormTestResult
        fields = "__all__"
        widgets = {
            "order_date": DateInput(format='%d.%m.%Y', attrs={'class': 'form-control datefield'}),
            "test_date": DateInput(format='%d.%m.%Y', attrs={'class': 'form-control datefield'}),
            "result_date": DateInput(format='%d.%m.%Y', attrs={'class': 'form-control datefield'}),
            "isolation_end": DateInput(format='%d.%m.%Y', attrs={'class': 'form-control datefield'}),
            "doc": FileInput(attrs={'accept': 'application/pdf'}),
        }


class FormIsolationModalForm(BSModalModelForm):
    class Meta:
        model = FormIsolation
        fields = "__all__"
        widgets = {
            "order_date": DateInput(format='%d.%m.%Y', attrs={'class': 'form-control datefield'}),
            "start_date": DateInput(format='%d.%m.%Y', attrs={'class': 'form-control datefield'}),
            "end_date": DateInput(format='%d.%m.%Y', attrs={'class': 'form-control datefield'}),
            "doc": FileInput(attrs={'accept': 'application/pdf'}),
        }
