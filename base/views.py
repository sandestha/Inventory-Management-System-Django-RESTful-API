from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from .models import User, Category, Product, Customer, Supplier, Order, Warehouse, Shipment
from .serializers import UserSerializer,CategorySerializer,ProductSerializer,CustomerSerializer,SupplierSerializer,OrderSerializer,WarehouseSerializer,ShipmentSerializer
# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(username=email,password=password)

    if user == None:
        return Response('Invalid Credentials !!!')
    else:
        token,_ = Token.objects.get_or_create(user=user)
        return Response(token.key)
    

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        password = request.data.get('password')
        hash_password = make_password(password)
        obj = serializer.save()
        obj.password = hash_password
        obj.save()
        return Response('USer Created !!')
    else:
        return Response('serializer.errors')


class CategoryApiView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductApiView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fields = ['category__name','category']
    search_fields = ['name']

class CustomerApiView(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class SupplierApiView(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class OrderApiView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class WarehouseApiView(ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer

class ShipmentApiView(ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer