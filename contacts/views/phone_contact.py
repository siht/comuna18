from django.views.generic import (
    detail,
    edit,
    list as _list,
)
from django.urls import reverse_lazy
from ..models import (
    Contact,
    ContactPhone
)

__all__ = (
    'ContactPhoneListView',
    'ContactPhoneView',
    'ContactPhoneCreateView',
)


class OwnPhonesMixin:
    def get_queryset(self):
        contact_phones = (
            self.model.objects
            .filter(
                contact_id=self.kwargs.get('contact_pk')
            )
        )
        return contact_phones


class ContactPhoneListView(OwnPhonesMixin, _list.ListView):
    model = ContactPhone

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        contact_id = self.kwargs.get('contact_pk')
        contact = Contact.objects.get(id=contact_id)
        context.update(contact=contact)
        return context


class ContactPhoneView(OwnPhonesMixin, detail.DetailView):
    model = ContactPhone


class ContactPhoneCreateView(edit.CreateView):
    model = ContactPhone
    fields = ['phone_number']
    success_url = reverse_lazy('contact-list')

    def form_valid(self, form):
        contact_pk = self.kwargs.get('contact_pk')
        current_contact = Contact.objects.get(pk=contact_pk)
        form.instance.contact = current_contact
        return super().form_valid(form)
