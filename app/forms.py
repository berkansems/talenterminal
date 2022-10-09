from django import forms

from .models import Developers, Clients

class ClientsCreateForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ['name', 'email', 'description', 'position']

    def __init__(self, *args, **kwargs):
        super(ClientsCreateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'specials'}
