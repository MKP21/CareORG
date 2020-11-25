from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import mixins

from care_api import serializers
from care_api import models
from care_api import permissions


# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating a user"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email', 'is_organisation')


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


# to logout, remove the token on client side
# class UserLogoutApiView(APIView):
#     """Handle user logout"""
#
#     def get(self, request):
#         """Delete User Token"""
#         try:
#             request.user.auth_token.delete()
#         except (AttributeError, ObjectDoesNotExist):
#             pass
#
#         request.user.Authorization = None
#         return Response(status=status.HTTP_200_OK)
#
#     def post(self, request, format=None):
#         """Delete User Token"""
#
#         request.user.Authorization = None
#         return Response(status=status.HTTP_200_OK)

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handle creating,reading and updating profile feed items"""
    authentication_classes = {TokenAuthentication, }
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnFeed,
        IsAuthenticated
    )

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)


class OrgDetailsViewSet(viewsets.ModelViewSet):
    """Handle organisation details"""
    authentication_classes = {TokenAuthentication, }
    serializer_class = serializers.OrgDetailsSerializer
    queryset = models.OrgDetails.objects.all()
    permission_classes = (
        permissions.UpdateOwnDetails,
        IsAuthenticated,
    )

    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)


class DonationHistoryViewSet(viewsets.ModelViewSet):
    """Handle donation records"""
    authentication_classes = {TokenAuthentication, }
    serializer_class = serializers.DonationHistorySerializer
    queryset = models.DonationHistory.objects.all()
    permission_classes = (
        IsAuthenticated,
    )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user_profile', 'event_id')