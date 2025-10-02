from django.contrib import admin

from teams.models import Team, TeamMembership, Position


class TeamMembershipInline(admin.TabularInline):
    model = TeamMembership
    extra = 1


class PositionAdmin(admin.ModelAdmin):
    fields = ['name',]
    list_display = ['name', ]
    list_display_links = ['name', ]


class TeamMembershipAdmin(admin.ModelAdmin):
    fields = ['member', 'team', 'role']
    list_display = ['member', 'team', 'role']
    list_display_links = ['member', 'team']
    list_filter = ['team', 'role']


class TeamAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'logo', 'owner']
    list_display = ['name', 'owner', 'created_at']
    list_display_links = ['name', 'owner']
    list_filter = ['created_at', 'owner']
    inlines = [TeamMembershipInline]


admin.site.register(Position, PositionAdmin)
admin.site.register(TeamMembership, TeamMembershipAdmin)
admin.site.register(Team, TeamAdmin)
