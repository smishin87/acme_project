from django import forms

from .models import Birthday


class BirthdayForm(forms.ModelForm):

    class Meta:
        fields = '__all__'
        model = Birthday
        widgets = {
            'birthday': forms.DateInput({'type': 'date'}),
        }