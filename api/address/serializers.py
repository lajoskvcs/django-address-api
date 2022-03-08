from rest_framework import serializers

from api.models import Address


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = (
            "id",
            "name",
            "country",
            "state",
            "postal_code",
            "city",
            "address_1",
            "address_2",
            "created_at",
            "updated_at",
        )
