from django import forms
from django.utils.encoding import force_unicode
from django.utils.html import escape, conditional_escape
from .models import Event, Property, Icon, Color, Note, Alert

from itertools import chain

class mySelect(forms.Select):

    def __init__(self, attrs=None, choices=()):
        super(forms.Select, self).__init__(attrs)
        # choices can be any iterable, but we may need to render this widget
        # multiple times. Thus, collapse it into a list so it can be consumed
        # more than once.
        self.choices = list(choices)

    def render_options(self, choices, selected_choices):
        def render_option(option_value, option_label):
            option_value = force_unicode(option_value)
            selected_html = (option_value in selected_choices) and u' selected="selected"' or ''
            split = option_label.split('-'); # custom by JUN
            return u'<option color="%s" value="%s"%s>%s</option>' % (
                conditional_escape(force_unicode(split[1])), escape(option_value), selected_html,
                conditional_escape(force_unicode(split[0])))
        # Normalize to strings.
        selected_choices = set([force_unicode(v) for v in selected_choices])
        output = []
        for option_value, option_label in chain(self.choices, choices):
            if isinstance(option_label, (list, tuple)):
                output.append(u'<optgroup label="%s">' % escape(force_unicode(option_value)))
                for option in option_label:
                    output.append(render_option(*option))
                output.append(u'</optgroup>')
            else:
                output.append(render_option(option_value, option_label))
        return u'\n'.join(output)

class PropertyCreateForm(forms.ModelForm):

    class Meta:
        model = Property
        fields = ("name", "description", "address", "icon_type", "icon_color")

    name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
           'placeholder': 'Property Name'})
        )

    description = forms.CharField(
        max_length=255, 
        widget=forms.Textarea(attrs={
           'placeholder': 'Input property description here...'}), 
        required=False)

    address = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
           'placeholder': 'Address'}),
        required=False
        )
    icon_type = forms.ModelChoiceField(queryset=Icon.objects.all())
    icon_color = forms.ModelChoiceField(queryset=Color.objects.all(), widget=mySelect())

class FileUploadForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )


class EventCreateForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ("name", "comment")

    name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
           'placeholder': 'Event Name'}),
        required=True)

    comment = forms.CharField(
        max_length=30,
        widget=forms.Textarea(attrs={
           'placeholder': 'Add a comment here...'})
        )

class NoteCreateForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ("name", "comment")

    name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
           'placeholder': 'Note Name'}),
        required=True)

    comment = forms.CharField(
        max_length=30,
        widget=forms.Textarea(attrs={
           'placeholder': 'Add a comment here...'})
        )


class AlertCreateForm(forms.ModelForm):

    class Meta:
        model = Alert
        fields = ("comment", 'when')

    comment = forms.CharField(
        max_length=30)

    when = forms.DateTimeField(
        required=True,
        widget=forms.DateInput(format=('%Y-%m-%d'),
                                attrs={'type':'date'})
        )
