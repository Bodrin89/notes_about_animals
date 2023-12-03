from rest_framework.permissions import BasePermission

from apps.blogs.models import Blog


class OwnerPermission(BasePermission):
    def has_object_permission(self, request, view, obj: Blog):
        user = request.user
        owner = obj.user
        return user == owner
