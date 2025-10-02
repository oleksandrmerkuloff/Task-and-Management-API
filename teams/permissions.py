from rest_framework.permissions import BasePermission, SAFE_METHODS

from teams.models import Team


class TeamPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True

        if request.method in SAFE_METHODS:
            return request.user.is_authenticated

        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or request.user == obj.leader:
            return True

        if request.method in SAFE_METHODS:
            return obj.members.filter(id=request.user.id).exists()

        return False


class MembershipPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True

        if request.method in SAFE_METHODS:
            return request.user.is_authenticated

        if request.method == 'POST':
            team_id = request.data.get('team')
            if not team_id:
                return False

            try:
                team = Team.objects.get(id=team_id)
            except Team.DoesNotExist:
                return False

            return request.user == team.leader

        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or request.user == obj.team.leader:
            return True

        if request.method in SAFE_METHODS:
            return obj.team.members.filter(id=request.user.id).exists()

        return False
