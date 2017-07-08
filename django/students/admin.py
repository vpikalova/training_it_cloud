from django.contrib import admin

from .models import Student


# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Persoal info', {'fields': ['name', 'surname', 'date_of_birth']}),
        ('Contct info', {'fields': ['email', 'phone', 'address', 'skype']}),
        (None, {'fields':['courses']}),
    ]

    list_display = ('fullname', 'email', 'skype')
    search_fields = ['surname','email']
    list_filter = ['courses']

admin.site.register(Student, StudentAdmin)