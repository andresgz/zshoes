# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework import serializers

from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    """
    Serializer for Article Model
    """
    store = serializers.ReadOnlyField(source='store.name')

    class Meta:
        model = Article
