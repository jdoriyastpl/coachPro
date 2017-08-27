from rest_framework import permissions

class IsAuthenticatedOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read permission - always allow for GET request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions - only if authenticated
        return request.user and request.user.is_authenticated()
