from django.http import Http404
from django.shortcuts import render

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Order
from .serializers import OrderSerializer


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
    serializer = OrderSerializer(data=request.data)
    
    if serializer.is_valid():

        serializer.save(user=request.user,)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LatestOrdersList(APIView):
    def get(self, request, format=None):
        products = Order.objects.all()[0:1000000]
        serializer = OrderSerializer(products, many=True)
        return Response(serializer.data)

class OrderDetail(APIView):
    def get_object(self, randomID):
        try:
            return Order.objects.get(randomID=randomID)
        except Order.DoesNotExist:
            raise Http404
    
    def get(self, request, randomID, format=None):
        product = self.get_object(randomID)
        serializer = OrderSerializer(product)
        return Response(serializer.data)

class UserOrdersList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)