from django.db import models

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_usuario


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Subscripcion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario.nombre_usuario} -> {self.categoria.nombre}"


class ObjetoColeccionable(models.Model):
    OFERTA_CHOICES = [
        ('venta', 'Venta'),
        ('intercambio', 'Intercambio'),
        ('compra', 'Compra'),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='imagenes/')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    ofertado_por = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo_oferta = models.CharField(max_length=20, choices=OFERTA_CHOICES)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
