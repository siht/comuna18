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


class ContactEmailView(detail.DetailView):
    model = ContactEmail
