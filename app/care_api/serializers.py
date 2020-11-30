from rest_framework import serializers
from care_api import models


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password', 'is_organisation')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and Return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
            is_organisation=validated_data['is_organisation'],
        )

        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes the profile feed item"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'event_title', 'event_description', 'created_on', 'expires_on', 'is_Expired',
                  'goal_amount',
                  'received_amount')
        extra_kwargs = {'user_profile': {'read_only': True}}


class OrgDetailsSerializer(serializers.ModelSerializer):
    """Serializes the organisation details"""

    class Meta:
        model = models.OrgDetails
        fields = ('id', 'user_profile', 'description', 'location', 'industry')


class DonationHistorySerializer(serializers.ModelSerializer):
    """Serializes a donation transaction"""

    class Meta:
        model = models.DonationHistory
        fields = ('id', 'user_profile', 'event_id', 'amount_donated')

# class DonationSerializer(serializers.ModelSerializer):
#     """Serializes the donation amount"""
#
#     class Meta:
#         model = models.ProfileFeedItem
#         fields = ('received_amount',)
