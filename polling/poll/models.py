from django.db import models


class TimeStamped(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Polling(TimeStamped):
    soap_know = models.BooleanField(default=False, null=True, blank=True)
    soap_unknown = models.BooleanField(default=False, null=True, blank=True)
    soap_worked = models.BooleanField(default=False, null=True, blank=True)

    rest_know = models.BooleanField(default=False, null=True, blank=True)
    rest_unknown = models.BooleanField(default=False, null=True, blank=True)
    rest_worked = models.BooleanField(default=False, null=True, blank=True)

    django_know = models.BooleanField(default=False, null=True, blank=True)
    django_unknown = models.BooleanField(default=False, null=True, blank=True)
    django_worked = models.BooleanField(default=False, null=True, blank=True)

    graphql_know = models.BooleanField(default=False, null=True, blank=True)
    graphql_unknown = models.BooleanField(default=False, null=True, blank=True)
    graphql_worked = models.BooleanField(default=False, null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

