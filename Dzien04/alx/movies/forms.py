# Definicja formularza

from django import forms
from .models import *

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"

# formularz bez połaczenia z modelem bazodanowym
class ContactForm(forms.Form):
    SUBJECT_LIST = (
        (0, 'Issue'),
        (1, 'Error')
    )
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=255)
    urgent = forms.BooleanField(label="Sprawa pilna")
    message = forms.CharField(
        max_length=1024, widget=forms.Textarea(), help_text="Opisz dokładnie problem"
    )
    subject = forms.ChoiceField(choices=SUBJECT_LIST)

