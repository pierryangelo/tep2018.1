from rest_framework import permissions


class IsPostOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.profile.user == request.user


class IsAuthenticated(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return obj.profile.user.is_authenticated
