from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """User can only update their own profile, not other's profile"""
    def has_object_permission(self, request, view, obj):        

        if request.method in permissions.SAFE_METHODS:
            return True
    
        return obj.id == request.user.id



class UpdateMovieInfo(permissions.BasePermission):
    """Only the post owner can update the post info"""
    def has_object_permission(self, request, view, obj):        
        
        if request.method in permissions.SAFE_METHODS:
            return True
    
        return obj.user_profile.id == request.user.id
