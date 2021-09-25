from django.contrib import admin

# Register your models here.
from review.models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'headline',
        'ticket',
        'user',
        'rating',
    )