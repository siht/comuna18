from django.urls import path
from .views import (
    ContactListView,
    ContactView,
    ContactCreateView,
    ContactUpdateView,
    ContactPhoneView,
    ContactEmailView,
    ContactEmailListView,
    ContactEmailCreateView,
)


urlpatterns = [
    path('', ContactListView.as_view(), name='contact-list'),
    path('<pk>', ContactView.as_view(), name='contact-detail'),
    path('new/', ContactCreateView.as_view(), name='contact-create'),
    path('edit/<pk>', ContactUpdateView.as_view(), name='contact-update'),
    path('<contact_pk>/phone/<pk>', ContactPhoneView.as_view(), name='phone-detail'),
    path('<contact_pk>/mail/', ContactEmailListView.as_view(), name='email'),
    path('<contact_pk>/mail/<pk>', ContactEmailView.as_view(), name='email-detail'),
    path('<contact_pk>/mail/create/', ContactEmailCreateView.as_view(), name='email-create'),
]