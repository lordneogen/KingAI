from django.contrib import admin
from .models import *


# Register your models here.
# {id: 1, name: 'Имя', title: 'Бла-Бла', money: 1000, popularity: 0, army: 0, land: -10},
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'money', 'popularity', 'army', 'land')


admin.site.register(Cards,MyModelAdmin)
admin.site.register(Trys)
admin.site.register(Kings)
admin.site.register(Num_edu)