from django.shortcuts import render

from .forms import Birthday
from .utils import calculate_birthday_countdown
from .models import BirthdayForm


def birthday(request):
    form = Birthday(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        form.save()
        birthday_countdown = calculate_birthday_countdown(
            form.cleaned_data['birthday']
        )
        context.update({'birthday_countdown': birthday_countdown})
    return render(request, 'birthday/birthday.html', context=context)


def birthday_list(request):
    birthdays = BirthdayForm.objects.all()
    context = {'birthdays': birthdays}
    return render(request, 'birthday/birthday_list.html', context=context)
