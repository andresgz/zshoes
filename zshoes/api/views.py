# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.http import Http404

from rest_framework import generics

from zshoes.stores.serializers import StoreSerializer
from zshoes.stores.models import Store
from zshoes.articles.models import Article
from zshoes.articles.serializers import ArticleSerializer

from .mixins import CustomListRendererMixin


class StoreListView(CustomListRendererMixin, generics.ListAPIView):
    """
    List of stores
    """
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class ArticleListView(CustomListRendererMixin, generics.ListAPIView):
    """
    List of articles
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticlesFromStoreListView(CustomListRendererMixin, generics.ListAPIView):
    """
    List of articles
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_queryset(self):
        queryset = super(ArticlesFromStoreListView, self).get_queryset()
        store_id = self.kwargs.get('pk')

        if not store_id.isdigit():
            raise ValueError('Bad Request')
        try:
            store = Store.objects.get(id=store_id)
        except Store.DoesNotExist:
            raise Http404('Record not Found')

        queryset = queryset.filter(store=store)
        return queryset
