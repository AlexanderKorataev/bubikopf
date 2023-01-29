from rest_framework import serializers

from .models import Product, Products


class ProductSerializer(serializers.ModelSerializer):

    class Meta:

        model = Product
        fields = (
            'id', 
            'ru_name',
            'en_name', 
            'get_absolute_url', 
            'ru_description',
            'en_description', 
            'ru_price',
            'en_price',
            'get_image',
            'get_thumbnail',
            'video_duration',
            'video_file_id'
        )

class ProductsSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Products
        fields = (
            "products",
        )