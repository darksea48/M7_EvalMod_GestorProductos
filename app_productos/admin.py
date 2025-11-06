from django.contrib import admin
from .models import Producto, Categoria, Etiqueta, DetalleProducto

# Inline para DetalleProducto (OneToOne relationship)
class DetalleProductoInline(admin.StackedInline):
    model = DetalleProducto
    extra = 0  # No crear automáticamente
    max_num = 1  # Solo un detalle por producto
    can_delete = True
    fields = ('peso', 'ancho', 'alto', 'largo')

# Admin para Producto
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'categoria', 'fecha_creacion')
    list_filter = ('categoria', 'etiquetas', 'fecha_creacion')
    search_fields = ('nombre', 'descripcion')
    filter_horizontal = ('etiquetas',)
    inlines = [DetalleProductoInline]
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'descripcion', 'precio')
        }),
        ('Relaciones', {
            'fields': ('categoria', 'etiquetas')
        }),
    )

# Admin para Categoria
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

# Admin para Etiqueta
@admin.register(Etiqueta)
class EtiquetaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

# Admin para DetalleProducto (opcional, ya está como inline)
@admin.register(DetalleProducto)
class DetalleProductoAdmin(admin.ModelAdmin):
    list_display = ('producto', 'peso', 'ancho', 'alto', 'largo')
    list_filter = ('peso',)
