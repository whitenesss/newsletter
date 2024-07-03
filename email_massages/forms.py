from django.forms import ModelForm

from clients.forms import StyleFormMixin
from email_massages.models import EmailMessage


class EmailMassage(StyleFormMixin, ModelForm):
    class Meta:
        model = EmailMessage
        exclude = ('owner',)


class ManagerEmailMassageForm(StyleFormMixin, ModelForm):
    class Meta:
        model = EmailMessage
        fields = ('status',)
