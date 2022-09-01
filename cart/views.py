import imp
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from cart import serializers
from .models import Cart
# Create your views here.


class CartApiView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]


    def post(self, request):
        serializer = serializers.CartSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
    
    def get(sself, request):
        carts = Cart.objects.all()
        serializer = serializers.CartListSerializer(carts, many=True).data
        return Response(serializer, status=200)