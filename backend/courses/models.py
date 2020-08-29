from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Courses(models.Model):
    """Курсы"""
    name = models.CharField('Название', max_length=140)
    url = models.URLField('Ссылка', max_length=140, unique=True)
    rating = models.PositiveSmallIntegerField('Рейтинг', null=True, blank=True,
            validators=[MinValueValidator(0), MaxValueValidator(5)],
            choices=[(i, i) for i in range(6)])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['name']
