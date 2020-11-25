from django.urls import path, include
from rest_framework.routers import DefaultRouter
from care_api import views

router = DefaultRouter()
router.register('user', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)
router.register('details', views.OrgDetailsViewSet)
router.register('history', views.DonationHistoryViewSet)

urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]
