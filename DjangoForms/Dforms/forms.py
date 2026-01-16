from django import forms
from .models import Dforms


class registerform(forms.ModelForm):

    class Meta:
        model = Dforms
        fields ="__all__"
        # fields=['uid','username','email','password']
        # exclude=['role']



