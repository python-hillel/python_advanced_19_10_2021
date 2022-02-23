from django.contrib import admin

from students.models import Students

from .models import Group


class StudentsInlineTable(admin.TabularInline):
    model = Students
    fields = [
        'first_name',
        'last_name',
        'birthday',
        'phone_number',
    ]

    extra = 0


class TeacherInlineTable(admin.TabularInline):
    model = Group.teachers.through
    extra = 0


class GroupAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'start_date',
        'end_date',
        'headman',
    ]

    fields = [
        'name',
        ('start_date', 'end_date'),
        'headman',
        'teachers',
    ]

    inlines = [StudentsInlineTable, TeacherInlineTable]


admin.site.register(Group, GroupAdmin)
