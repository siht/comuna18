from django.views.generic import (
    detail,
    edit,
    list as _list,
)
from django.urls import reverse_lazy
from ..models import ContactEmail

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


class ContactEmailView(detail.DetailView, OwnMailsMixin):
    model = ContactEmail
