from api.base.annotations.viewsets import WorldBorderVeiws
from rest_framework import routers
from .accounts.users.viewsets import (
    UserViewSet
)
router = routers.DefaultRouter()

# account
router.register('users', UserViewSet, basename='user-viewsets')
router.register('annotations', WorldBorderVeiws, basename='annotation-viewsets')

urls = router.urls