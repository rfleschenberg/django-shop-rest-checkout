from rest_framework.serializers import ModelSerializer, Serializer


class CheckoutSerializer(Serializer):
    pass


class ShippingAddressSerializer(ModelSerializer):
    pass


class BillingAddressSerializer(ModelSerializer):
    pass
