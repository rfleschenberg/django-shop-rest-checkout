import test_project.serializers
from test_project.models import ShippingAddress


def test_shipping_address_serializer():
    address = ShippingAddress(name='René')
    serializer = test_project.serializers.ShippingAddressSerializer(address)
    assert serializer.data['name'] == 'René'
