from django import forms
from .models import Event, Note

class EventCreateForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ("name", "comment")

    name = forms.CharField(
        max_length=30,
        required=True)

    comment = forms.CharField(
        max_length=30)

class NoteCreateForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ("name", "comment")

    name = forms.CharField(
        max_length=30,
        required=True)

    comment = forms.CharField(
        max_length=30)
