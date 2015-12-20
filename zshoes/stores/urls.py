# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from .views import StoreListView, StoreUpdateView, StoreCreateView


urlpatterns = [
    url(r'^$', StoreListView.as_view(), name="list"),
    url(r'^create$', StoreCreateView.as_view(), name="create"),
    url(r'^update/(?P<pk>\d+)/$', StoreUpdateView.as_view(), name="update"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
