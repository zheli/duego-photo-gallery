from apps.rest_api.fields import PasswordField, HyperlinkedImageField
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = PasswordField(required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')
