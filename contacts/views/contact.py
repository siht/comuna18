from django.contrib.auth.mixins import LoginRequiredMixin
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


class ContactListView(LoginRequiredMixin, OwnContactsMixin, _list.ListView):
    model = Contact
    login_url = reverse_lazy('auth_login')
    redirect_field_name = 'redirect_to'


class ContactView(LoginRequiredMixin, OwnContactsMixin, detail.DetailView):
    model = Contact
    login_url = reverse_lazy('auth_login')
    redirect_field_name = 'redirect_to'


class ContactCreateView(LoginRequiredMixin, edit.CreateView):
    model = Contact
    fields = ['name']
    success_url = reverse_lazy('contacts:contact-list')
    login_url = reverse_lazy('auth_login')
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        current_user = self.request.user
        form.instance.user = current_user
        return super().form_valid(form)


class ContactUpdateView(LoginRequiredMixin, edit.UpdateView):
    model = Contact
    fields = ['name']
    success_url = reverse_lazy('contacts:contact-list')
    login_url = reverse_lazy('auth_login')
    redirect_field_name = 'redirect_to'
