from .bulma_mixin import BulmaMixin
from django import forms

from .models import Dweller, STATUS_TYPES, Senior


class DwellerForm(BulmaMixin, forms.ModelForm):
    first_name = forms.CharField(label='Write first name')
    last_name = forms.CharField(label='Write last name')
    age = forms.IntegerField(label='Write age')
    social_status = forms.ChoiceField(choices=STATUS_TYPES, required=True, label='Choose social status')
    obeys_to = forms.ModelChoiceField(queryset=Senior.objects.all().order_by('-id'), label='Choose the senior')

    class Meta:
        model = Dweller
        fields = ['first_name', 'last_name', 'age', 'obeys_to', 'social_status', ]

