from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'Admin'

class IsUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'User'

# from rest_framework.permissions import BasePermission

# class IsAdmin(BasePermission):
#     """
#     Custom permission to only allow users with role 'admin' to access the view.
#     """

#     def has_permission(self, request, view):
#         return request.user.is_authenticated and request.user.role == 'admin'

# from rest_framework import permissions

# class IsAdminOrSelf(permissions.BasePermission):
#     """
#     Custom permission:
#     - Admins can do anything.
#     - Normal users can only access/modify their own record.
#     """

#     def has_permission(self, request, view):
#         # Admins always allowed
#         if request.user and request.user.is_staff:
#             return True

#         # For non-admins, only allow safe methods (GET, PUT, PATCH, DELETE) on their own object
#         return True  # Let object-level check handle restrictions

#     def has_object_permission(self, request, view, obj):
#         # Admins can do anything
#         if request.user and request.user.is_staff:
#             return True

#         # Non-admins can only act on themselves
#         return obj == request.user
