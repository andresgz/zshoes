from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from .models import Article


class ArticleListView(ListView):
    """
    View to list all the articles
    """
    #: Article model
    model = Article
    template_name = "articles/list.html"


class ArticleCreateView(CreateView):
    """
    View to create a Article
    """
    model = Article
    fields = ['name', 'store', 'description', 'price',
              'total_in_shelf', 'total_in_vault']
    template_name = "articles/create.html"
    success_url = reverse_lazy('articles:list')

    def form_valid(self, form):
        messages.success(
            self.request,
            _('Article {0} created'.format(form.cleaned_data['name'])))
        return super(ArticleCreateView, self).form_valid(form)


class ArticleUpdateView(UpdateView):
    """
    View to update a Article
    """
    model = Article
    fields = ['name', 'store', 'description', 'price',
              'total_in_shelf', 'total_in_vault']
    template_name = "articles/update.html"
    success_url = reverse_lazy('articles:list')

    def form_valid(self, form):
        messages.success(
            self.request,
            _('Article {0} updated'.format(form.cleaned_data['name'])))
        return super(ArticleUpdateView, self).form_valid(form)
