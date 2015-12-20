# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework import serializers

from .models import Store


class StoreSerializer(serializers.ModelSerializer):
    """
    Serializer for Store model
    """
    class Meta:
        model = Store
