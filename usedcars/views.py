from rest_framework import generics
from usedcars.models import Field, Car
from usedcars.serializers import FieldSerializer, CarSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from usedcars.permissions import IsOwnerOrIsAdminOrReadOnly, IsAdminUserOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'cars': reverse('car-list', request=request, format=format),
        'users': reverse('user-list', request=request, format=format),
        'fields': reverse('field-list', request=request, format=format)
    })


class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrIsAdminOrReadOnly,)


class FieldList(generics.ListCreateAPIView):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer

    permission_classes = (IsAdminUserOrReadOnly,)


class FieldDetail(generics.RetrieveUpdateAPIView):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer

    permission_classes = (IsAdminUserOrReadOnly,)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
