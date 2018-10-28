from django.views.generic import detail
from django.urls import reverse_lazy
from ..models import ContactPhone

__all__ = (
    'ContactPhoneView',
)


class ContactPhoneView(detail.DetailView):
    model = ContactPhone

    def get_queryset(self):
        contact_phones = (
            self.model.objects
            .filter(
                contact_id=self.kwargs.get('contact_pk')
            )
        )
        return contact_phones
