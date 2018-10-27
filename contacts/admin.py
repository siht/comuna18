from django.contrib import admin
from .models import (
    Contact,
    ContactPhone,
    ContactEmail,
)

admin.site.register(Contact)
admin.site.register(ContactPhone)
admin.site.register(ContactEmail)
