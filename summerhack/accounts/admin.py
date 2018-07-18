from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from accounts.models import Tree


#class TreeAdmin(admin.TabularInline):
#    model = Tree

#class IndicatorInline(admin.ModelAdmin):
#    inlines = [
#                TreeAdmin,
#              ]

admin.site.register(Tree)

