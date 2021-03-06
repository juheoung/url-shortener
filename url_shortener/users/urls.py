from django.urls import path
from rest_framework import routers
from users.views import UserViewSet

router = routers.SimpleRouter()
router.register('users', UserViewSet)
urlpatterns = router.urls
