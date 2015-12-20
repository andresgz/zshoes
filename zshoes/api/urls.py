# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from .views import StoreListView, ArticleListView, ArticlesFromStoreListView

urlpatterns = [
    url(r'^stores/$', StoreListView.as_view(), name="store_list"),
    url(r'^articles/$', ArticleListView.as_view(), name="article_list"),
    url(r'^articles/stores/(?P<pk>\w+)/?$',
        ArticlesFromStoreListView.as_view(), name="article_list"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
