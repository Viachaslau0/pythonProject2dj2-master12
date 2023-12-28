from django.contrib import admin
from .models import Category, FoodItem


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)


class FoodItemAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(FoodItem, FoodItemAdmin)
