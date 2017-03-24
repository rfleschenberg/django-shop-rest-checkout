from django.contrib.auth import get_user_model

import pytest

import test_project.serializers
from test_project.models import Customer, ShippingAddress


@pytest.fixture
def customer():
    User = get_user_model()
    user = User.objects.create(username='rene')
    customer = Customer.objects.create(user=user)
    return customer


@pytest.mark.django_db
def test_shipping_address_serializer(customer):
    address = ShippingAddress.objects.create(name='René', customer=customer)
    serializer = test_project.serializers.ShippingAddressSerializer(address)
    assert serializer.data['name'] == 'René'
