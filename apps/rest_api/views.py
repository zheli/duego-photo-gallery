from apps.rest_api.serializers import UserSerializer
from apps.rest_api.viewsets import CreateModelViewSet, CreateListModelViewSet
from django.contrib.auth.models import User
from rest_framework import permissions

class UserRegisterView(CreateModelViewSet):
    """
    API endpoint for user registration
    """
    queryset = User.objects.all
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PhotoUploadListView(CreateListModelViewSet):
    """
    API endpoint for photo upload and listing
    """
    queryset = Photo.objects.all
    serializer_class = PhotoSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
