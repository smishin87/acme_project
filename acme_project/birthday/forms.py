from django import forms

from .models import BirthdayForm


class Birthday(forms.ModelForm):

    class Meta:
        fields = '__all__'
        model = BirthdayForm
        widgets = {
            'birthday': forms.DateInput({'type': 'date'}),
        }