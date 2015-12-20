# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from .views import ArticleListView, ArticleUpdateView, ArticleCreateView


urlpatterns = [
    url(r'^$', ArticleListView.as_view(), name="list"),
    url(r'^create$', ArticleCreateView.as_view(), name="create"),
    url(r'^update/(?P<pk>\d+)/$', ArticleUpdateView.as_view(), name="update"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
