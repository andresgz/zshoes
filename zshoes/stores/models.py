from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Store(models.Model):
    """
    Entity that represents the stores where articles are located
    """
    #: Name of the Store
    name = models.CharField(max_length=45)
    # Complete address of the store
    address = models.TextField(null=True, blank=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
