from django.contrib import admin

from EShopApp.models import VideoGame


# Register your models here.
class VideoGameAdmin(admin.ModelAdmin):
    pass

admin.site.register(VideoGame, VideoGameAdmin)
