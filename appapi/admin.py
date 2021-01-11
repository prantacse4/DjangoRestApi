from django.contrib import admin
from .models import MyApi

# Register your models here.


@admin.register(MyApi)
class NotesAdmin(admin.ModelAdmin):
    list_display = ('id','fullname', 'code', 'mobile')