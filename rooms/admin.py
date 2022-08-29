from atexit import register
from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models
# Register your models here.

@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = ("name", "user_by")

    def user_by(self, obj):
        return obj.rooms.count()

    
    pass

class PhotoInline(admin.TabularInline):

    model = models.Photo




@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    
    """ Room Admin Definition """

    inlines = (PhotoInline,)

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        # (
        #     "More About the Space",
        #     {
        #         # "classes": ("collapse",),
        #         "fields": ("amenities", "facilities", "house_rules"),
        #     },
        # ),
        ("Last Details", {"fields": ("host",)}),
    )


    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )



    list_filter = (
        "instant_book",  
        "room_type", 
        "amenities", 
        "facility", 
        "house_rule",
        "city", 
        "country",
    )

    raw_id_fields = ("host",)

    search_fields = ("=city", "^host__username")

    filter_horizontal = ("amenities", "facility", "house_rule")

    def count_amenities(self, obj):
        return obj.amenities.count()
    
    def count_photos(self, obj):
        return obj.photos.count()





@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    list_display = ('__str__', "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"