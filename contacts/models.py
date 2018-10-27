from django.db import models
from django.core.validators import RegexValidator
from django.urls import reverse

__all__ = (
    'Contact',
    'ContactPhone',
    'ContactEmail',
)


class Contact(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=128)

    def get_absolute_url(self):
        return reverse('contact-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class ContactPhone(models.Model):
    contact = models.ForeignKey('Contact', on_delete=models.CASCADE)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list

    def __str__(self):
        return self.phone_number


class ContactEmail(models.Model):
    contact = models.ForeignKey('Contact', on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return self.email
