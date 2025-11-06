from django import forms
from .models import *

class ProductoForm(forms.ModelForm):
    # Campos del modelo DetalleProducto incluidos en el formulario de Producto
    peso = forms.DecimalField(
        max_digits=8, 
        decimal_places=2, 
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Peso en kg'})
    )
    ancho = forms.DecimalField(
        max_digits=8, 
        decimal_places=2, 
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ancho en cm'})
    )
    alto = forms.DecimalField(
        max_digits=8, 
        decimal_places=2, 
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Alto en cm'})
    )
    largo = forms.DecimalField(
        max_digits=8, 
        decimal_places=2, 
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Largo en cm'})
    )
    
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'categoria', 'etiquetas']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'etiquetas': forms.CheckboxSelectMultiple(),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Si estamos editando, cargar los datos de DetalleProducto
        if self.instance and self.instance.pk:
            try:
                # Usar 'detalle' en lugar de 'detalles' según el related_name
                detalle = self.instance.detalle
                self.fields['peso'].initial = detalle.peso
                self.fields['ancho'].initial = detalle.ancho
                self.fields['alto'].initial = detalle.alto
                self.fields['largo'].initial = detalle.largo
            except DetalleProducto.DoesNotExist:
                # No existe detalle para este producto
                pass
    
    def save(self, commit=True):
        producto = super().save(commit=False)
        
        if commit:
            producto.save()
            
            # Guardar las etiquetas (ManyToMany)
            self.save_m2m()
            
            # Crear o actualizar DetalleProducto
            detalle_data = {
                'peso': self.cleaned_data.get('peso'),
                'ancho': self.cleaned_data.get('ancho'),
                'alto': self.cleaned_data.get('alto'),
                'largo': self.cleaned_data.get('largo'),
            }
            
            # Solo crear/actualizar si hay al menos un campo con datos
            if any(detalle_data.values()):
                try:
                    # Verificar si ya existe un detalle para este producto
                    detalle = producto.detalle
                    # Actualizar el detalle existente
                    for field, value in detalle_data.items():
                        setattr(detalle, field, value)
                    detalle.save()
                except DetalleProducto.DoesNotExist:
                    # Crear nuevo detalle
                    DetalleProducto.objects.create(
                        producto=producto,
                        **detalle_data
                    )
        
        return producto

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'required': False}),
        }

class EtiquetaForm(forms.ModelForm):
    class Meta:
        model = Etiqueta
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }