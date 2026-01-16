from django import forms
from .models import cars

class carforms(forms.ModelForm):
    class Meta:
        model = cars
        fields = "__all__"
        # exclude = ['price']
        # fields = ['username', 'email', 'password']