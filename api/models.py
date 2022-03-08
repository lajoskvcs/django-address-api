from django.db import models
from django_countries.fields import CountryField


class Address(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name of the address")
    country = CountryField()
    state = models.CharField(max_length=100, verbose_name="State/Province")
    postal_code = models.CharField(max_length=100, verbose_name="ZIP/Postal code")
    city = models.CharField(max_length=100, verbose_name="City")
    address_1 = models.CharField(max_length=100, verbose_name="Address")
    address_2 = models.CharField(max_length=100, verbose_name="Apartment, suite, etc.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        "auth.User",
        related_name="addresses",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.user.username + ' - ' + self.name

    class Meta:
        unique_together = [
            [
                "country",
                "state",
                "postal_code",
                "city",
                "address_1",
                "address_2",
                "user",
            ],
            [
                "user",
                "name"
            ]
        ]
