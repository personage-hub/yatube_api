from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        is_safe = request.method in permissions.SAFE_METHODS
        is_auth = request.user.is_authenticated
        return is_auth or is_safe

    def has_object_permission(self, request, view, obj):
        is_safe = request.method in permissions.SAFE_METHODS
        is_author = obj.author == request.user
        return is_author or is_safe
