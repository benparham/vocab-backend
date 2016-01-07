from rest_framework import permissions

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS', 'POST')

class UserPermission(permissions.IsAuthenticatedOrReadOnly):
    def has_permission(self, request, view):
        if (request.method in SAFE_METHODS):
            return True

        return super(UserPermission, self).has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        if (request.method in SAFE_METHODS):
            return True

        return obj == request.user
