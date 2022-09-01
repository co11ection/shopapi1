from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, response
from . import serializers
from .models import Product
from rest_framework.decorators import action
from rating.serializers import ReviewSerializer

# Create your views here.

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ProductListSerializer
        return serializers.PrductDetailSerializer
    
    @action(['GET', 'POST'], detail=True)
    def reviews(self, request, pk=None):
        product = self.get_object()
        if request.method=='GET':
            reviews = product.reviews.all()
            serializer = ReviewSerializer(reviews, many=True).data
            return response.Response(serializer, status=200)
        data = request.data
        serializer = ReviewSerializer(data=data, context={'request':request, 'product':product})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status= 201)