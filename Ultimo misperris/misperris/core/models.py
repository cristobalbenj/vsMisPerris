from django.db import models

# Create your models here.
class Raza(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Raza"
        verbose_name_plural = "Razas" 


class Estado(models.Model):
    tipoEstado = models.CharField(max_length=15)

    def __str__(self):
        return self.tipoEstado

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"

class Genero(models.Model):
    genero = models.CharField(max_length=15)

    def __str__(self):
        return self.genero

    class Meta:
        verbose_name = "Genero"
        verbose_name_plural = "Generos"


class Mascota(models.Model):
    nombre = models.CharField(max_length=25)
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    imagen = models.FileField(upload_to='photo')
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
         return self.nombre

    class Meta:
        verbose_name = "Mascota"
        verbose_name_plural = "Mascotas"


class GeneroAdoptante(models.Model):
    genero = models.CharField(max_length=15)

    def __str__(self):
        return self.genero

    class Meta:
        verbose_name = "Genero"
        verbose_name_plural = "Generos"


class Region(models.Model):
    idRegion = models.IntegerField()
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.idRegion


class Ciudad(models.Model):
    idCiudad = models.IntegerField()
    nombre = models.CharField(max_length=80)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.idCiudad


class tipoVivienda(models.Model):
    idTipo = models.IntegerField()
    descripcion = models.CharField(max_length=30)

    def __str__(self):
        return self.idTipo


class Adoptante(models.Model):
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    tel = models.IntegerField(max_length=8)
    direccion = models.CharField(max_length=80)
    genero = models.ForeignKey(GeneroAdoptante, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)

    def __str__(self):
        return self.rut


















