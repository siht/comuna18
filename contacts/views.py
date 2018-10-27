from django.views.generic import detail
from .models import (
    Contact,
    ContactPhone,
    ContactEmail,
)

__all__ = (
    'ContactView',
    'ContactPhoneView',
    'ContactEmailView',
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
