from rest_framework import mixins, generics
# Create your views here.
class CreateModelViewSet(mixins.CreateModelViewSet, generics.GenericAPIView):
    pass

class CreateListModelViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
        generics.GenericAPIView):
    pass
