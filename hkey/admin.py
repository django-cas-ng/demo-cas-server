from django.contrib import admin

# Register your models here.

from .models import Huser, Grouper, MemberOf

admin.site.register(Huser)
admin.site.register(Grouper)
admin.site.register(MemberOf)
