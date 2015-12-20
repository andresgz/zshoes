from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from zshoes.stores.models import Store


@python_2_unicode_compatible
class Article(models.Model):
    """
    Entity that represents the articles of the store
    """
    #: Name of the Article
    name = models.CharField(max_length=45)
    #: Description of the Article
    description = models.TextField(null=True, blank=True)
    #: Price of the Article
    price = models.FloatField()
    #: Available articles in shelf
    total_in_shelf = models.PositiveIntegerField(default=0)
    #: Available articles in vault
    total_in_vault = models.PositiveIntegerField(default=0)
    #: Store of the article
    store = models.ForeignKey(Store)

    def __str__(self):
        return self.name
