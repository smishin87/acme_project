from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from .validators import real_age


User = get_user_model()


class Tag(models.Model):
    tag = models.CharField('Тег', max_length=20)

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.tag


class BirthdayModel(models.Model):
    tag = models.ManyToManyField(
        Tag,
        verbose_name='Теги',
        blank=True,
        help_text='Удерживайте Ctrl для выбора нескольких вариантов'
    )
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


class Congratulation(models.Model):
    text = models.TextField('Текст поздравления')
    birthday = models.ForeignKey(
        BirthdayModel,
        on_delete=models.CASCADE,
        related_name='congratulations',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('created_at',)

