from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """A user can edit only their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user making request is the owner"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.id == obj.id


class UpdateOwnFeed(permissions.BasePermission):
    """Allow organisations to update their feed"""

    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update their own feed"""

        if request.method in ('POST', 'DELETE') and obj.user_profile.id != request.user.id:
            return False

        return True


class UpdateOwnDetails(permissions.BasePermission):
    """Allow organisations to update their profile"""

    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update their profile and are an organisation"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
