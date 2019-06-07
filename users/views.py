from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import BasePermission
from .serializers import UserSerializer


class UserViewset(ModelViewSet):

    class IsOwnerOrReadOnly(BasePermission):
        def has_object_permission(self, request, view, obj):
            return bool(obj == request.user)

    permission_classes = (IsOwnerOrReadOnly,)
    queryset = User.objects.order_by('-date_joined')
    serializer_class = UserSerializer
    lookup_field = 'username'

