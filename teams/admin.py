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
    fields = ['member', 'team', 'position', 'experience']
    list_display = ['member', 'team', 'position']
    list_display_links = ['member', 'team']
    list_filter = ['team', 'position', 'experience']


class TeamAdmin(admin.ModelAdmin):
    fields = ['name', 'leader']
    list_display = ['name', 'leader', 'created_at']
    list_display_links = ['name', 'leader']
    list_filter = ['created_at', 'leader']
    inlines = [TeamMembershipInline]


admin.site.register(Position, PositionAdmin)
admin.site.register(TeamMembership, TeamMembershipAdmin)
admin.site.register(Team, TeamAdmin)
