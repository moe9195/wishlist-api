from rest_framework.permissions import BasePermission

class IsItemAdder(BasePermission):
    message = "You must be the user who added this item."

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or (obj.added_by == request.user):
            return True
        return False
