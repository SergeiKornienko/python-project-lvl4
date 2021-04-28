from datetime import datetime
from django.utils import timezone
from django.db import models


class Status(models.Model):
    """Statuses."""
    name = models.CharField('Имя', max_length=100, unique=True)
    created_at = models.DateTimeField('created_at', default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Стaтусы'


