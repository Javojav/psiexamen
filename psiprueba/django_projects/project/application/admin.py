from django.contrib import admin
from .models import Canal, Usuario, Suscripcion

# Register your models here.
@admin.register(Canal)
class canalAdmin(admin.ModelAdmin):
    pass

@admin.register(Usuario)
class usuarioAdmin(admin.ModelAdmin):
    pass

@admin.register(Suscripcion)
class suscripcionAdmin(admin.ModelAdmin):
    pass