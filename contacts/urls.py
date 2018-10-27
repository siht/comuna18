from django.urls import path
from .views import (
    ContactView,
    ContactPhoneView,
    ContactEmailView,
    ContactListView,
)


urlpatterns = [
    path('', ContactListView.as_view(), name='contact-list'),
    path('<pk>', ContactView.as_view(), name='contact-detail'),
    path('<contact_pk>/phone/<pk>', ContactPhoneView.as_view(), name='phone-detail'),
    path('<contact_pk>/mail/<pk>', ContactEmailView.as_view(), name='email-detail'),
]