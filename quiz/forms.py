from django import forms
from django.forms import ModelForm
from . models import Question as data
from accounts.models import User
from django.db import models

OPTIONS = (
    ('option-a', data.optionA),
    ('option-b', data.optionB),
    ('option-c', data.optionC),
    ('option-d', data.optionD),
)
class QuizForm(forms.Form):
    options = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class':'option'}), choices=OPTIONS)

class SettingsForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'avatar']