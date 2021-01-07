from bootstrap_modal_forms.forms import BSModalModelForm

from front.models import FormTestOrder, FormTestResult, FormIsolation


# TODO: remove if unnecessary
class FormTestOrderModalForm(BSModalModelForm):
    class Meta:
        model = FormTestOrder
        fields = "__all__"


class FormTestResultModalForm(BSModalModelForm):
    class Meta:
        model = FormTestResult
        fields = "__all__"


class FormIsolationModalForm(BSModalModelForm):
    class Meta:
        model = FormIsolation
        fields = "__all__"
