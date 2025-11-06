from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Categorías"
    
    def __str__(self):
        return self.nombre


class Etiqueta(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    
    class Meta:
        verbose_name_plural = "Etiquetas"
    
    def __str__(self):
        return self.nombre


class DetalleProducto(models.Model):
    # Relación Uno a Uno: Un detalle pertenece a un único producto
    producto = models.OneToOneField(
        'Producto',
        on_delete=models.CASCADE,
        related_name='detalle',
        primary_key=True
    )
    peso = models.DecimalField(max_digits=8, decimal_places=2, help_text="Peso en kg", blank=True, null=True)
    ancho = models.DecimalField(max_digits=8, decimal_places=2, help_text="Ancho en cm", blank=True, null=True)
    alto = models.DecimalField(max_digits=8, decimal_places=2, help_text="Alto en cm", blank=True, null=True)
    largo = models.DecimalField(max_digits=8, decimal_places=2, help_text="Largo en cm", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Detalles de Productos"
    
    def __str__(self):
        return f"Detalles de {self.producto.nombre} - {self.peso}kg"


class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Relación Muchos a Uno: Muchos productos pertenecen a una categoría
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.SET_NULL, 
        related_name='productos',
        null=True,
        blank=True
    )
    
    # Relación Muchos a Muchos: Un producto puede tener muchas etiquetas
    etiquetas = models.ManyToManyField(
        Etiqueta, 
        related_name='productos',
        blank=True  # Permite que no tenga etiquetas
    )
    


    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    class Meta:
        ordering = ['-fecha_creacion']
    
    def __str__(self):
        return self.nombre