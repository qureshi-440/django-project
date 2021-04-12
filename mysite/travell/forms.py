from .models import Destination
from django import forms

class destination_form(forms.ModelForm):
    class Meta:
        model = Destination
        fields = "__all__"
