from apps.core.models import Photo
from apps.rest_api.fields import PasswordField, HyperlinkedImageField
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = PasswordField(required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')

class PhotoSerializer(serializers.ModelSerializer):
    user = serializers.Field()
    image = HyperlinkedImageField()

    class Meta:
        model = Photo
