from django import forms
from .models import Event

class EventCreateForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ("name", "comment")

    name = forms.CharField(
        max_length=30,
        required=True)

    comment = forms.CharField(
        max_length=30)
