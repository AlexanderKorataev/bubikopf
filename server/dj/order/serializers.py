from rest_framework import serializers

from .models import Order

class OrderSerializer(serializers.ModelSerializer):

    class Meta:

        model = Order
        fields = (
            'id', 
            'name', 
            'product_id', 
            'user_id',
            'paid_amount',
            'get_payment_url',
            'get_payment_status',
            'payment_id',
            'randomID'
        )