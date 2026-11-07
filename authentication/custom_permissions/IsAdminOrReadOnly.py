from rest_framework.permissions import SAFE_METHODS,BasePermission


class IsAdminOrReadOnly(BasePermission):
    message='Creating or editing events is restricted to Admins only.'
    def has_permission(self, request, view):
        # if user makes a GET,HEAD,OPTIONS request
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_staff