from django.urls import path, include
from rest_framework.routers import DefaultRouter

from care_api import views

router = DefaultRouter()
router.register('user', views.UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
