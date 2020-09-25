from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """A user can edit only their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user making request is the owner"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.id == obj.id