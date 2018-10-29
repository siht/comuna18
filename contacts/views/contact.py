from django.views.generic import (
    detail,
    edit,
    list as _list,
)
from django.urls import reverse_lazy
from ..models import Contact

__all__ = (
    'ContactListView',
    'ContactView',
    'ContactCreateView',
    'ContactUpdateView',
)


class OwnContactsMixin:
    def get_queryset(self):
        own_contacts = (
            self.model.objects
            .filter(
                user=self.request.user
            )
        )
        return own_contacts


class ContactListView(OwnContactsMixin, _list.ListView):
    model = Contact


class ContactView(OwnContactsMixin, detail.DetailView):
    model = Contact


class ContactCreateView(edit.CreateView):
    model = Contact
    fields = ['name']
    success_url = reverse_lazy('contacts:contact-list')

    def form_valid(self, form):
        current_user = self.request.user
        form.instance.user = current_user
        return super().form_valid(form)


class ContactUpdateView(edit.UpdateView):
    model = Contact
    fields = ['name']
    success_url = reverse_lazy('contacts:contact-list')
