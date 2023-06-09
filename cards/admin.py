from django.contrib import admin
from cards.models import movieCards
# Register your models here.

class cardadmin(admin.ModelAdmin):
    list_display=("photo","title","descript","update","link")
admin.site.register(movieCards,cardadmin)