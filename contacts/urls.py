from django.urls import path
from .views import (
    ContactView,
    ContactPhoneView,
    ContactEmailView,
)

urlpatterns = [
    path('<pk>', ContactView.as_view(), name='contact-detail'),
    path('<pk>', ContactPhoneView.as_view(), name='phone-detail'),
    path('<pk>', ContactEmailView.as_view(), name='email-detail'),
]