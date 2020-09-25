from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from care_api import serializers
from care_api import models

# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating a user"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

