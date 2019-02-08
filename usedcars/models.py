from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField

TYPE_CHOICES = (('char', 'char'), ('text', 'text'), ('datetime', 'datetime'), ('date', 'date'), ('float', 'float'),
                ('integer', 'integer'), ('boolean', 'boolean'))


class Field(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, unique=True)
    type = models.CharField(choices=TYPE_CHOICES, max_length=30)
    length = models.PositiveIntegerField(null=True)
    options = ArrayField(models.CharField(max_length=30), null=True)

    class Meta:
        ordering = ['created']


class Car(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    data = JSONField()
    owner = models.ForeignKey('auth.User', related_name='cars', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created']
