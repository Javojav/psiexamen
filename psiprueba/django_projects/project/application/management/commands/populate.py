from django.core.management.base import BaseCommand
from django.apps import apps


from application.models import Canal, Usuario, Suscripcion

## ESTE IMPORT NO APARECE EN ZNOTAS
from datetime import datetime


class Command(BaseCommand):
    # definimos info
    canales = [
        {
            "id": 1001,
            "nombreCanal": "elxokasTV"
        },
        {
            "id": 1002,
            "nombreCanal": "ibai"
        },
        {
            "id": 1003,
            "nombreCanal": "playz"
        }
    ]

    usuarios = [
        {
            "id": 1001,
            "nombreUsuario": "antonio2985"
        },
        {
            "id": 1002,
            "nombreUsuario": "respetaCamiones124" 
        },
        {
            "id": 1003,
            "nombreUsuario": "asierUR"
        }
    ]

    suscripciones = [
        {
            "id": 1001,
            "canal": 1001,
            "usuario": 1001,
            "fechaDeSuscripcion": "05-04-2023"
        },
        {
            "id": 1002,
            "canal": 1001,
            "usuario": 1002,
            "fechaDeSuscripcion": "11-04-2023"
        },
        {
            "id": 1003,
            "canal": 1003,
            "usuario": 1003,
            "fechaDeSuscripcion": "12-04-2023"
        }
    ]

    # esto es para luego meter las cosas en suscriptions
    createdCanales = []
    createdUsuarios = []
    createdSuscripciones = []

    def handle(self, *args, **options):
        self.cleanDataBase()
        self.canal()
        self.usuario()
        self.suscripcion()

    def cleanDataBase(self):
        Canal.objects.all().delete()
        Usuario.objects.all().delete()
        Suscripcion.objects.all().delete()
    
    def canal(self):
        canal = Canal.objects.all()

        for canal in self.canales:
            canal = Canal(id=canal["id"],
                          nombreCanal=canal["nombreCanal"])
            canal.save()

            # guardamos en array para que luego tal
            self.createdCanales.append(canal)
        


    def usuario(self):
        usuario = Usuario.objects.all()

        for usuario in self.usuarios:
            usuario = Usuario(id=usuario["id"],
                              nombreUsuario=usuario["nombreUsuario"])
            usuario.save()

            # guardamos en array para que luego tal hazlo en el examen y ya bro no rayes jai
            self.createdUsuarios.append(usuario)

    def suscripcion(self):
        suscripcion = Suscripcion.objects.all()

        for suscripcion in self.suscripciones:
            canal = Canal.objects.get(id=suscripcion["canal"])
            usuario = Usuario.objects.get(id=suscripcion["usuario"])

            suscripcion = Suscripcion(
                id=suscripcion["id"],
                canal=canal,
                usuario=usuario,
                fechaDeSuscripcion=datetime.strptime(suscripcion["fechaDeSuscripcion"], "%d-%m-%Y").strftime("%Y-%m-%d")
            )

            suscripcion.save()

            # guardamos en array para que luego tal hazlo en el examen y ya bro no rayes jai
            self.createdSuscripciones.append(suscripcion)
    