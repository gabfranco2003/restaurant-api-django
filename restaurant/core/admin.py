from django.contrib import admin
from .models import UserProfile, MenuItem  # Ensure MenuItem is imported

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'date_of_birth')  # Columns to display in the admin list view
    search_fields = ('user__username', 'phone')        # Add a search bar
    list_filter = ('date_of_birth',)                   # Add filters for specific fields

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'image')  # Add 'image' to the admin view
    list_filter = ('category',)   

# Correct registration of models
admin.site.register(UserProfile, UserProfileAdmin)  # Register UserProfile with UserProfileAdmin
admin.site.register(MenuItem, MenuItemAdmin)        # Register MenuItem with MenuItemAdmin
