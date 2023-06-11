from django.contrib import admin

# Register your models here.
from webseries.models import webcards
# Register your models here.

class webadmin(admin.ModelAdmin):
    list_display=("w_photo","w_title","w_descript","w_update","w_link")
admin.site.register(webcards,webadmin)