from django.contrib import admin
from todoapp.models import Studentdata

# Register your models here.
class StudentdataAdmin(admin.ModelAdmin):
    list_display=['name','rollno','marks']

admin.site.register(Studentdata,StudentdataAdmin)
