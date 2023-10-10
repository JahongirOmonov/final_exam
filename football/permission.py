from rest_framework.permissions import BasePermission

class AdminPermissionClass(BasePermission):
    def has_permission(self, request, view):
        if request.user.roles == 3:
            return True
        return False 
    
class OwnerStadiumPermissionClass(BasePermission):
    def has_permission(self, request, view):
        if request.user.roles == 2:
            return True
        return False 
class UserPermissionClass(BasePermission):
    def has_permission(self, request, view):
        if request.user.roles == 1:
            return True
        return False 


class OwnerPermissionClass(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.id==obj.user.id:
            return True
        return False

class AdminOrOwnerStadiumPermissionClass(BasePermission):
    def has_permission(self, request, view):
        if request.user.roles == 2 or request.user.roles == 3:
            return True
        return False 
    
class AdminOrUserPermissionClass(BasePermission):
    def has_permission(self, request, view):
        if request.user.roles == 1 or request.user.roles == 3:
            return True
        return False

