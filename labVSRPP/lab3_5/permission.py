from django.contrib.auth.models import Group
from rest_framework import permissions


def _is_in_group(user, group_name):
    """
    Takes a user and a group name, and returns `True` if the user is in that group.
    """
    try:
        print(
            f"{Group.objects.get(name=group_name)} gg {Group.objects.get(name=group_name).user_set.all()} userid {user.id}")
        return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()
    except Group.DoesNotExist:
        return None


def _has_group_permission(user, required_groups):
    return any([_is_in_group(user, group_name) for group_name in required_groups])


class IsLoggedInUserOrAdmin(permissions.BasePermission):
    # group_name for super admin
    required_groups = ['admin']

    def has_object_permission(self, request, view, obj):
        has_group_permission = _has_group_permission(request.user, self.required_groups)
        if self.required_groups is None:
            return False
        return obj == request.user or has_group_permission


class IsAdminUser(permissions.BasePermission):
    # group_name for super admin
    required_groups = ['admin']

    def has_permission(self, request, view):
        has_group_permission = _has_group_permission(request.user, self.required_groups)
        return request.user and has_group_permission

    def has_object_permission(self, request, view, obj):
        has_group_permission = _has_group_permission(request.user, self.required_groups)
        return request.user and has_group_permission


class IsAdminOrAnonymousUser(permissions.BasePermission):
    required_groups = ['admin', 'student']

    def has_permission(self, request, view):
        has_group_permission = _has_group_permission(request.user, self.required_groups)
        return request.user and has_group_permission

class IsOwnerOrAdmin(permissions.BasePermission):
    # group_name for super admin
    required_groups = ['admin']

    def has_object_permission(self, request, view, obj):
        has_group_permission = _has_group_permission(request.user, self.required_groups)
        if self.required_groups is None:
            print('6666666666666666666666666')
            return False
        print('fgggggggggggggggggggggggggggggggggggggggggggggg')
        return obj.user == request.user or has_group_permission
# def has_permission(self, request, view):
#     has_group_permission = _has_group_permission(request.user, self.required_groups)
#     if has_group_permission:
#         return True
#     else:
#         print('fdghgfhghgh')
#         return view.action in ['retrieve', 'update', 'partial_update', 'destroy']
