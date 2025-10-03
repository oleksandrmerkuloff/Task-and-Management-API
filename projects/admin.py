from django.contrib import admin

from projects.models import Project, Task


class TaskInline(admin.StackedInline):
    model = Task
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'deadline', 'status', 'team')
    list_display = ('name', 'created_at', 'deadline', 'status')
    list_display_links = ('name',)
    list_filter = ('team', 'status', 'deadline',)
    search_fields = ('name', 'team')
    inlines = [
        TaskInline,
    ]


class TaskAdmin(admin.ModelAdmin):
    fields = ('name', 'content', 'deadline', 'status', 'project')
    list_display = ('name', 'created_at', 'deadline', 'project', 'status')
    list_display_links = ('name',)
    list_filter = ('project', 'status', 'deadline')
    search_fields = ('name', 'project',)


admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
