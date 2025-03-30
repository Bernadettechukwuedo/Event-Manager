from rest_framework import permissions


class IsAuthororReadonly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == permissions.SAFE_METHODS:
            return True
        return obj.created_by == request.user
