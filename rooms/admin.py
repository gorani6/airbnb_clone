from atexit import register
from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = ("name", "user_by")

    def user_by(self, obj):
        return obj.rooms.count()

    
    pass




@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    
    """ Room Admin Definition """

    # fieldsets = (
    #     (
    #         "Basic Info", 
    #         {"fields" : ("name", "description", "country", "address", "price")},
    #     ),
    #     ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
    #     ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
    #     (
    #         "More About the Space",
    #         {
    #             "classes": ("collapse",),
    #             "fields": ("amenities", "facilities", "house_rules"),
    #         },
    #     ),
    #     ("Last Details", {"fields": ("host",)}),
    # )

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


    search_fields = ("=city", "^host__username")

    filter_horizontal = ("amenities", "facility", "house_rule")

    def count_amenities(self, obj):
        return obj.amenities.count()
    
    def count_photos(self, obj):
        return obj.photos.count()





@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ """

    pass