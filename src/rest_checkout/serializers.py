from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import Serializer


class CheckoutSerializer(Serializer):
    pass


class ShippingAddressSerializer(ModelSerializer):
    pass


class BillingAddressSerializer(ModelSerializer):
    pass
