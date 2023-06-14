from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, \
    DetailView

from .forms import BirthdayForm
from .models import BirthdayModel
from .utils import calculate_birthday_countdown


class BirthdayMixin:
    model = BirthdayModel
    form_class = BirthdayForm
    template_name = 'birthday/birthday.html'


class BirthdayCreateView(BirthdayMixin, CreateView):
    pass


class BirthdayListView(ListView):
    model = BirthdayModel
    template_name = 'birthday/birthday_list.html'
    ordering = 'id'
    paginate_by = 5


class BirthdayUpdateView(BirthdayMixin, UpdateView):
    pass


class BirthdayDeleteView(DeleteView):
    model = BirthdayModel
    template_name = 'birthday/birthday_confirm_delete.html'
    success_url = reverse_lazy('birthday:list')


class BirthdayDetailView(DetailView):
    model = BirthdayModel
    template_name = 'birthday/birthday_detail.html'

    def get_context_data(self, **kwargs):
        # Получаем словарь контекста:
        context = super().get_context_data(**kwargs)
        # Добавляем в словарь новый ключ:
        context['birthday_countdown'] = calculate_birthday_countdown(
            # Дату рождения берём из объекта в словаре context:
            self.object.birthday
        )
        # Возвращаем словарь контекста.
        return context
