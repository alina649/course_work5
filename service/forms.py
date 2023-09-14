from django import forms

from service.models import Mailing


class MailingForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ('commence_time', 'completion_time', 'frequency', 'message', 'client')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(MailingForm, self).__init__(*args, **kwargs)