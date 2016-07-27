from django import forms
from .models import Event, Property, Icon, Color

class PropertyCreateForm(forms.ModelForm):

    class Meta:
        model = Property
        fields = ("name", "description", "address", "icon_type", "icon_color")

    name = forms.CharField(
        max_length=30)

    description = forms.CharField(max_length=255, widget=forms.Textarea, required=False)

    address = forms.CharField(
        max_length=100,required=False)

    icon_type = forms.ModelChoiceField(queryset=Icon.objects.all(),required=False)
    icon_color = forms.ModelChoiceField(queryset=Color.objects.all(),required=False)



class EventCreateForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ("name", "comment", 'id')

    name = forms.CharField(
        max_length=30,
        required=True)

    comment = forms.CharField(
        max_length=30)

    id = forms.CharField(
        widget=forms.HiddenInput()
    )
