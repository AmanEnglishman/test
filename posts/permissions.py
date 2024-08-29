from rest_framework.permissions import BasePermission


class IsPostAuthorOrIsStaff(BasePermission):
    """
    Custom permission to only allow authors of a post or users with is_staff status to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        # Check if the user is staff
        if request.user.is_staff:
            return True

        # Check if the user is the author of the post
        return obj.user == request.user
