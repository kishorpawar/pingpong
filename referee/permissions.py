from rest_framework import permissions

class RefereePermission(permissions.BasePermission):
	message = "Only Refree can create a game."

	def has_permission(self, request, view):
		groups = request.user.groups.all().values_list('name', flat=True)
		
		return True if "referee" in groups else False
