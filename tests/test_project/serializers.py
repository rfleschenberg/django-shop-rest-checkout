import rest_checkout.serializers as base

from .models import ShippingAddress


class ShippingAddressSerializer(base.ShippingAddressSerializer):
    class Meta:
        model = ShippingAddress
        fields = ('name', )
