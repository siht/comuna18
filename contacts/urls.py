from django.urls import path
from .views import (
    ContactListView,
    ContactView,
    ContactCreateView,
    ContactUpdateView,
    ContactPhoneView,
    ContactEmailView,
)


urlpatterns = [
    path('', ContactListView.as_view(), name='contact-list'),
    path('<pk>', ContactView.as_view(), name='contact-detail'),
    path('new/', ContactCreateView.as_view(), name='contact-create'),
    path('edit/<pk>', ContactUpdateView.as_view(), name='contact-create'),
    path('<contact_pk>/phone/<pk>', ContactPhoneView.as_view(), name='phone-detail'),
    path('<contact_pk>/mail/<pk>', ContactEmailView.as_view(), name='email-detail'),
]