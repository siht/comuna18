from django.views.generic import (
    detail,
    edit,
    list as _list,
)
from django.urls import reverse_lazy
from ..models import (
    Contact,
    ContactEmail
)

__all__ = (
    'ContactEmailView',
    'ContactEmailListView',
)

class OwnMailsMixin:
    def get_queryset(self):
        contact_emails_accounts = (
            self.model.objects
            .filter(
                contact_id=self.kwargs.get('contact_pk')
            )
        )
        return contact_emails_accounts


class ContactEmailListView(_list.ListView, OwnMailsMixin):
    model = ContactEmail

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        contact_id = self.kwargs.get('contact_pk')
        contact = Contact.objects.get(id=contact_id)
        context.update(contact=contact)
        return context


class ContactEmailView(detail.DetailView, OwnMailsMixin):
    model = ContactEmail
