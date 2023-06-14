from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from .validators import real_age


User = get_user_model()


class BirthdayModel(models.Model):
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField(
        'Фамилия',
        blank=True,
        help_text='Необязательное поле',
        max_length=20
    )
    birthday = models.DateField(
        'Дата рождения',
        validators=(real_age,)
    )
    image = models.ImageField('фото', blank=True, upload_to='birthday_images')
    author = models.ForeignKey(
        User, verbose_name='Автор записи', on_delete=models.CASCADE, null=True
    )

    def get_absolute_url(self):
        # С помощью функции reverse() возвращаем URL объекта.
        return reverse('birthday:detail', kwargs={'pk': self.pk})

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('first_name', 'last_name', 'birthday'),
                name='Unique person constraint',
            ),
        )