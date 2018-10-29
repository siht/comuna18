from django.contrib.auth.mixins import LoginRequiredMixin
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
    'ContactPhoneUpdateView',
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


class ContactPhoneListView(LoginRequiredMixin, OwnPhonesMixin, _list.ListView):
    model = ContactPhone
    login_url = reverse_lazy('auth_login')
    redirect_field_name = 'redirect_to'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        contact_id = self.kwargs.get('contact_pk')
        contact = Contact.objects.get(id=contact_id)
        context.update(contact=contact)
        return context


class ContactPhoneView(LoginRequiredMixin, OwnPhonesMixin, detail.DetailView):
    model = ContactPhone
    login_url = reverse_lazy('auth_login')
    redirect_field_name = 'redirect_to'


class ContactPhoneCreateView(LoginRequiredMixin, edit.CreateView):
    model = ContactPhone
    fields = ['phone_number']
    success_url = reverse_lazy('contacts:contact-list')
    login_url = reverse_lazy('auth_login')
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        contact_pk = self.kwargs.get('contact_pk')
        current_contact = Contact.objects.get(pk=contact_pk)
        form.instance.contact = current_contact
        return super().form_valid(form)


class ContactPhoneUpdateView(LoginRequiredMixin, edit.UpdateView):
    model = ContactPhone
    fields = ['phone_number']
    success_url = reverse_lazy('contacts:contact-list')
    login_url = reverse_lazy('auth_login')
    redirect_field_name = 'redirect_to'
