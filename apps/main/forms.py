from django import forms
from .models import Event, Property, Icon, Color, Note

class PropertyCreateForm(forms.ModelForm):

    class Meta:
        model = Property
        fields = ("name", "description", "address", "icon_type", "icon_color")

    name = forms.CharField(
        max_length=30)

    description = forms.CharField(max_length=255, widget=forms.Textarea, required=False)

    address = forms.CharField(
        max_length=100,required=False)

    icon_type = forms.ModelChoiceField(queryset=Icon.objects.all())#, widget=forms.Select(attrs={'style': "font-family: 'FontAwesome', Helvetica"}))
    icon_color = forms.ModelChoiceField(queryset=Color.objects.all())



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
