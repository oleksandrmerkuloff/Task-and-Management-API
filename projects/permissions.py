from rest_framework.permissions import BasePermission, SAFE_METHODS

from projects.models import Project


class ProjectPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user.is_staff

        if request.method in SAFE_METHODS:
            return request.user.is_authenticated

        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True

        if request.method in SAFE_METHODS:
            return (
                request.user == obj.team.leader
                or request.user in obj.team.members.all()
            )

        if request.method in ['POST', 'PATCH', 'DELETE']:
            return request.user == obj.team.leader

        return False


class TaskPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True

        if view.action == 'create' or view.action == 'list':
            project_id = request.data.get('project')
            if project_id is None:
                return False
            try:
                project = Project.objects.get(id=project_id)
            except Project.DoesNotExist:
                return False
            return (
                request.user == project.team.leader
                or request.user in project.team.members.all()
            )

        if view.action == 'list':
            return True

        return False

    def has_object_permission(self, request, view, obj):
        return (
            request.user.is_staff
            or request.user == obj.project.team.leader
            or request.user in obj.project.team.members.all()
            )
