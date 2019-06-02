from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer


class UserViewset(ModelViewSet):
    queryset = User.objects.order_by('-date_joined')
    serializer_class = UserSerializer
