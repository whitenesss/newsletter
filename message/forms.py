from django.forms import ModelForm, ValidationError

from clients.forms import StyleFormMixin
from message.models import Message


class MessageForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Message
        exclude = ('owner',)

        def clean_title(self):
            cleaned_data = self.cleaned_data['title']
            forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'обман']
            for word in forbidden_words:
                if word in cleaned_data.lower():
                    raise ValidationError('Недопустимое слово в заголовке сообщения!')

            return cleaned_data

        def clean_message(self):
            cleaned_data = self.cleaned_data['message']
            forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'обман']
            for word in forbidden_words:
                if word in cleaned_data.lower():
                    raise ValidationError('Недопустимое слово в сообщении!')

            return cleaned_data
