from django.contrib.auth.models import User

from rest_framework.viewsets import ModelViewSet


from .permissions import IsOwner
from .serializers import UserSerializer


class UserViewset(ModelViewSet):
    permission_classes = (IsOwner,)
    queryset = User.objects.order_by('-date_joined')
    serializer_class = UserSerializer
    lookup_field = 'username'
