from rest_framework import routers
from .accounts.users.viewsets import (
    UserViewSet
)
router = routers.DefaultRouter()

# account
router.register('users', UserViewSet, basename='user-viewsets')

urls = router.urls