from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Status(models.Model):
    """Statuses."""
    name = models.CharField('Имя', max_length=100, unique=True)
    created_at = models.DateTimeField('created_at', default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Стaтусы'


class Task(models.Model):
    """Tasks."""
    name = models.CharField('Имя', max_length=100)
    created_at = models.DateTimeField('created_at', default=timezone.now)
    description = models.TextField('Описание', null=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='task_author',
        verbose_name='Автор',
    )
    performer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='task_performer',
        verbose_name='Исполнитель',
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        verbose_name='Статус',
    )
