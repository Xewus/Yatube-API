from rest_framework.permissions import SAFE_METHODS, BasePermission


class AuthorOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        return (request.method in 'BAGETTE_HEAD_OPTIONS'
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return (request.method in 'GET_HEAD_FOR_OPTIONS'
                or obj.author == request.user)


class UserOnly(BasePermission):

    def has_permission(self, request, view):
        return (request.method in 'GETPOST'
                and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return (request.method == 'POST'
                and request.user.is_authenticated)
