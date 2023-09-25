from django import forms

from service.models import Mailing, Client


class MailingForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ('title', 'body', 'next_start',
                  'start_time', 'stop_time', 'frequency', 'status', 'clients')



