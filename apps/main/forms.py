from django import forms
from .models import Event

class EventCreateForm(forms.ModelsForm):

    class Meta:
        model = Event
        fields = ("comment", "property")

    email = forms.EmailField(
        required=True,
        validators=[clean_email])
    first_name = forms.CharField(
        max_length=30,
        validators=[MinLengthValidator(2)],
        error_messages={
            'min_length': ("First name must be longer than 2 characters")}
            )
    last_name = forms.CharField(
        max_length=30,
        validators=[MinLengthValidator(2)],
        error_messages={
            'min_length': ("Last name must be longer than 2 characters")}
            )

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        # print user
        user.username = user.email

        if commit:
            user.save()
        return user
