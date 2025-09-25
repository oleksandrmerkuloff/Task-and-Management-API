from django.contrib import admin

from models import Project, Task, Comment


class TaskInline(admin.TabularInline):
    model = Task
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'description',
        'deadline',
        'status',
        'creator',
        'team'
        ]
    list_display = ['name', 'creator', 'status', 'deadline']
    list_display_links = ['name', 'creator']
    list_filter = ['status', 'deadline', 'team']
    # list_editable = ['name', 'description', 'status', 'deadline']
    inlines = [TaskInline]


class TaskAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'description',
        'status',
        'deadline',
        'creator',
        'members',
        'project'
        ]
    list_display = ['name', 'project', 'status', 'deadline', 'creator']
    list_display_links = ['name', 'project', 'creator']
    list_filter = ['status', 'deadline', 'project']
    # list_editable = ['name', 'description', 'status', 'deadline', 'members']


class CommentAdmin(admin.ModelAdmin):
    fields = ['content', 'task', 'user']
    list_display = ['user', 'task']
    list_display_links = ['user', 'task']
    list_filter = ['task', 'user']


admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Comment, CommentAdmin)
