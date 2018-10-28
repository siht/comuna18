from django.views.generic import (
    detail,
    edit,
    list as _list,
)
from django.urls import reverse_lazy
from .models import (
    Contact,
    ContactEmail,
    ContactPhone,
)

__all__ = (
    'ContactListView',
    'ContactView',
    'ContactCreateView',
    'ContractUpdateView',
    'ContactPhoneView',
    'ContactEmailView',
)


class ContactListView(_list.ListView):
    model = Contact


class ContactView(detail.DetailView):
    model = Contact


class ContactCreateView(edit.CreateView):
    model = Contact
    fields = ['name']
    success_url = reverse_lazy('contact-list')

    def form_valid(self, form):
        current_user = self.request.user
        form.instance.user = current_user
        return super().form_valid(form)


class ContractUpdateView(edit.UpdateView):
    model = Contact
    fields = ['name']
    success_url = reverse_lazy('contact-list')


class ContactPhoneView(detail.DetailView):
    model = ContactPhone

    def get_queryset(self):
        contact_phones = (
            self.model.objects
            .filter(
                contact_id=self.kwargs.get('contact_pk')
            )
        )
        return contact_phones


class ContactEmailView(detail.DetailView):
    model = ContactEmail

    def get_queryset(self):
        contact_emails_accounts = (
            self.model.objects
            .filter(
                contact_id=self.kwargs.get('contact_pk')
            )
        )
        return contact_emails_accounts
