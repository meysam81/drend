from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers


from .views import UserViewset

router = routers.DefaultRouter()
router.register('', UserViewset)

app_name = 'users'

urlpatterns = [
    path('', include(router.urls), name='users-root')
]
