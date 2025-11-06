from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView
from django.db.models import Count, Q
from django.db import models
from .models import *
from .forms import *

# Create your views here.

def sitio_admin(request):
    return redirect('/admin/')

# Vista para la página de inicio
class IndexView(TemplateView):
    template_name = 'index.html'

# Views para Productos
class ProductoListView(ListView):
    model = Producto
    template_name = 'list.html'
    context_object_name = 'productos'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['context'] = 'productos'
        return context

class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'form.html'
    success_url = reverse_lazy('lista_productos')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['context'] = 'productos'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "El producto ha sido creado exitosamente.")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Por favor, corrige los errores del formulario.")
        return super().form_invalid(form)
    
class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'form.html'
    success_url = reverse_lazy('lista_productos')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['context'] = 'productos'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "El producto ha sido actualizado exitosamente.")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Por favor, corrige los errores del formulario.")
        return super().form_invalid(form)

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'detail.html'
    context_object_name = 'producto'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['context'] = 'productos'
        return context

def buscar_productos(request):
    query = request.GET.get('query', '').strip()
    productos_encontrados = []
    
    if query:
        productos_encontrados = Producto.objects.filter(
            Q(nombre__icontains=query) |
            Q(descripcion__icontains=query) |
            Q(categoria__nombre__icontains=query) |
            Q(etiquetas__nombre__icontains=query)
        ).distinct()
    
    context = {
        'productos': productos_encontrados,
        'context': 'productos',
        'busqueda': query,
        'query': query,  # Para mantener el valor en el formulario
    }
    return render(request, 'list.html', context)

def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    messages.success(request, "El producto ha sido eliminado exitosamente.")
    return redirect('lista_productos')

# Views para Categorías
class CategoriaListView(ListView):
    model = Categoria
    template_name = 'list.html'
    context_object_name = 'categorias'

    def get_queryset(self):
        # Agregar el conteo de productos asociados a cada categoría
        return Categoria.objects.annotate(
            total_productos=Count('productos')
        ).order_by('nombre')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['context'] = 'categorias'
        return context

class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'form.html'
    success_url = reverse_lazy('lista_categorias')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['context'] = 'categorias'
        return context

    def form_valid(self, form):
        messages.success(self.request, "La categoría ha sido creada exitosamente.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Por favor, corrige los errores del formulario.")
        return super().form_invalid(form)

class CategoriaUpdateView(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'form.html'
    success_url = reverse_lazy('lista_categorias')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['context'] = 'categorias'
        return context

    def form_valid(self, form):
        messages.success(self.request, "La categoría ha sido actualizada exitosamente.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Por favor, corrige los errores del formulario.")
        return super().form_invalid(form)

class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = 'detail.html'
    context_object_name = 'categoria'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['context'] = 'categorias'
        return context

def eliminar_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    categoria.delete()
    messages.success(request, "La categoría ha sido eliminada exitosamente.")
    return redirect('lista_categorias')

class CategoriaProductosListView(ListView):
    model = Producto
    template_name = 'list.html'
    context_object_name = 'productos'

    def get_queryset(self):
        categoria_id = self.kwargs['pk']
        return Producto.objects.filter(categoria_id=categoria_id)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['context'] = 'productos'
        return context
# Views para Etiquetas
class EtiquetaListView(ListView):
    model = Etiqueta
    template_name = 'list.html'
    context_object_name = 'etiquetas'

    def get_queryset(self):
        # Agregar el conteo de productos asociados a cada etiqueta
        return Etiqueta.objects.annotate(
            total_productos=Count('productos')
        ).order_by('nombre')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['context'] = 'etiquetas'
        return context

class EtiquetaCreateView(CreateView):
    model = Etiqueta
    form_class = EtiquetaForm
    template_name = 'form.html'
    success_url = reverse_lazy('lista_etiquetas')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['context'] = 'etiquetas'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "La etiqueta ha sido creada exitosamente.")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Por favor, corrige los errores del formulario.")
        return super().form_invalid(form)

class EtiquetaUpdateView(UpdateView):
    model = Etiqueta
    form_class = EtiquetaForm
    template_name = 'form.html'
    success_url = reverse_lazy('lista_etiquetas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['context'] = 'etiquetas'
        return context

    def form_valid(self, form):
        messages.success(self.request, "La etiqueta ha sido actualizada exitosamente.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Por favor, corrige los errores del formulario.")
        return super().form_invalid(form)

def eliminar_etiqueta(request, id):
    etiqueta = Etiqueta.objects.get(id=id)
    etiqueta.delete()
    messages.success(request, "La etiqueta ha sido eliminada exitosamente.")
    return redirect('lista_etiquetas')