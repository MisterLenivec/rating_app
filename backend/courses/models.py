from django.db import models


class Courses(models.Model):
    name = models.CharField(max_length=140)
    url = models.URLField(max_length=140)
    rating = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
