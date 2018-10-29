from django.contrib.auth.mixins import LoginRequiredMixin
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
    'ContactEmailCreateView',
    'ContactEmailUpdateView',
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


class ContactEmailListView(LoginRequiredMixin, OwnMailsMixin, _list.ListView):
    model = ContactEmail
    login_url = reverse_lazy('auth_login')
    redirect_field_name = 'redirect_to'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        contact_id = self.kwargs.get('contact_pk')
        contact = Contact.objects.get(id=contact_id)
        context.update(contact=contact)
        return context


class ContactEmailView(LoginRequiredMixin, OwnMailsMixin, detail.DetailView):
    model = ContactEmail
    login_url = reverse_lazy('auth_login')
    redirect_field_name = 'redirect_to'


class ContactEmailCreateView(LoginRequiredMixin, edit.CreateView):
    model = ContactEmail
    fields = ['email']
    success_url = reverse_lazy('contacts:contact-list')
    login_url = reverse_lazy('auth_login')
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        contact_pk = self.kwargs.get('contact_pk')
        current_contact = Contact.objects.get(pk=contact_pk)
        form.instance.contact = current_contact
        return super().form_valid(form)


class ContactEmailUpdateView(LoginRequiredMixin, edit.UpdateView):
    model = ContactEmail
    fields = ['email']
    success_url = reverse_lazy('contacts:contact-list')
    login_url = reverse_lazy('auth_login')
    redirect_field_name = 'redirect_to'
