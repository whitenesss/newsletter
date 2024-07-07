from django.forms import ModelForm, CheckboxInput

from clients.models import Client


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, CheckboxInput):
                field.widget.attrs['class'] = 'form-control'


class ClientsForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Client
        exclude = ('owner',)

