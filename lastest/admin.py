from django.contrib import admin

# Register your models here.

from lastest.models import latestCards
# Register your models here.

class latestadmin(admin.ModelAdmin):
    list_display=("l_photo","l_title","l_descript","l_update","l_link")
admin.site.register(latestCards,latestadmin)