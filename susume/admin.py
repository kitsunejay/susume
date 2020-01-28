from django.contrib import admin
from .models import Job, Spell, Server, Slot, Ability, Equipment

# Register your models here.
admin.site.register(Job)
admin.site.register(Spell)
admin.site.register(Server)
admin.site.register(Slot)
admin.site.register(Ability)
admin.site.register(Equipment)