from rest_framework import serializers
from usedcars.models import Field, Car
from django.contrib.auth.models import User


class FieldSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Field
        fields = ('url', 'id', 'name', 'type', 'length', 'options')


class CarSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Car
        fields = ('url', 'id', 'data', 'owner')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    cars = serializers.HyperlinkedRelatedField(many=True, view_name='car-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'cars')
