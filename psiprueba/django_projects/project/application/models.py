from django.db import models

class Canal (models.Model):
    id = models.AutoField(primary_key=True)
    nombreCanal = models.CharField(max_length=50)

    def __str__(self):
        return self.nombreCanal
    
class Usuario (models.Model):
    id = models.AutoField(primary_key=True)
    nombreUsuario = models.CharField(max_length=50)

    def __str__(self):
        return self.nombreUsuario
    
class Suscripcion (models.Model):
    id = models.AutoField(primary_key=True)
    canal = models.ForeignKey(Canal, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fechaDeSuscripcion = models.DateField()

    def __str__(self):
        return self.canal.nombreCanal + " " + self.usuario.nombreUsuario + " " + str(self.fechaDeSuscripcion)