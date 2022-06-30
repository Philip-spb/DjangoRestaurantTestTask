from django.contrib import admin

from restaurant.models import FoodCategory, Food


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_ru',)


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_ru', 'is_publish')
    list_display_links = ('id', 'name_ru')
    list_editable = ('is_publish',)
