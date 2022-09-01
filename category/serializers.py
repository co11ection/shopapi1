
from rest_framework import serializers
from .models import Category
from product.serializers import ProductListSerializer


class CategoryListSerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField()
    class Meta:
        model = Category
        fields = '__all__'

    
    def to_representation(self, instance):
        repr =  super().to_representation(instance)
        repr['products'] = ProductListSerializer(instance.products.all(), many = True).data
        return repr


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'