from apps.core.models import Photo
from apps.rest_api.serializers import UserSerializer, PhotoSerializer
from apps.rest_api.viewsets import CreateModelViewSet, CreateListModelViewSet
from django.contrib.auth.models import User
from rest_framework import permissions

class UserRegisterView(CreateModelViewSet):
    """
    API endpoint for user registration
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PhotoUploadListView(CreateListModelViewSet):
    """
    API endpoint for photo upload and listing
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def pre_save(self, obj):
        obj.user = self.request.user

    def post(self, request, *args, **kwargs):
        request.DATA['user_id'] = self.request.user.id
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
