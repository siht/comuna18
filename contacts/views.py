from django.views.generic import detail, list as _list
from .models import (
    Contact,
    ContactPhone,
    ContactEmail,
)

__all__ = (
    'ContactView',
    'ContactPhoneView',
    'ContactEmailView',
    'ContactListView',
)


class ContactView(detail.DetailView):
    model = Contact


class ContactPhoneView(detail.DetailView):
    model = ContactPhone

    def get_queryset(self):
        query_set = (
            self.model.objects
            .filter(
                contact_id=self.kwargs.get('contact_pk')
            )
        )
        return query_set

class ContactEmailView(detail.DetailView):
    model = ContactEmail

    def get_queryset(self):
        query_set = (
            self.model.objects
            .filter(
                contact_id=self.kwargs.get('contact_pk')
            )
        )
        return query_set


class ContactListView(_list.ListView):
    model = Contact