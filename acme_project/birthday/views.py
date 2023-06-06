from django.shortcuts import render

from .forms import BirthdayForm


def birthday(request):
    context = {
        'form': BirthdayForm()
    }
    return render(request, 'birthday/birthday.html', context=context)