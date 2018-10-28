from django.views.generic import detail
from django.urls import reverse_lazy
from ..models import ContactEmail

__all__ = (
    'ContactEmailView',
)


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
