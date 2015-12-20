from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from .models import Store


class StoreListView(ListView):
    """
    View to list al the stores
    """
    #: Store model
    model = Store
    template_name = "stores/list.html"


class StoreCreateView(CreateView):
    """
    View to create a Store
    """
    model = Store
    fields = ['name', 'address']
    template_name = "stores/create.html"
    success_url = reverse_lazy('stores:list')

    def form_valid(self, form):
        messages.success(
            self.request,
            _('Store {0} created'.format(form.cleaned_data['name'])))
        return super(StoreCreateView, self).form_valid(form)


class StoreUpdateView(UpdateView):
    """
    View to update a Store
    """
    model = Store
    fields = ['name', 'address']
    template_name = "stores/update.html"
    success_url = reverse_lazy('stores:list')

    def form_valid(self, form):
        messages.success(
            self.request,
            _('Store {0} updated'.format(form.cleaned_data['name'])))
        return super(StoreUpdateView, self).form_valid(form)
