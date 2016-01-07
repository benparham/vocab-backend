from rest_framework import permissions

class UserPermission(permissions.IsAuthenticatedOrReadOnly):
    def has_permission(self, request, view):
        if (request.method == 'POST'):
            return True

        return super(UserPermission, self).has_permission(request, view)
