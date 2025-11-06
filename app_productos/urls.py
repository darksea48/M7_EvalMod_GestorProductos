from django.urls import path
from . import views

urlpatterns = [
    # Página de inicio
    path('', views.IndexView.as_view(), name='index'),
    path('sitio_admin/', views.sitio_admin, name='sitio_admin'),
    
    # Productos
    path('productos/', views.ProductoListView.as_view(), name='lista_productos'),
    path('productos/crear/', views.ProductoCreateView.as_view(), name='crear_producto'),
    path('productos/<int:pk>/', views.ProductoDetailView.as_view(), name='detalle_producto'),
    path('productos/<int:pk>/editar/', views.ProductoUpdateView.as_view(), name='editar_producto'),
    path('productos/<int:id>/eliminar/', views.eliminar_producto, name='eliminar_producto'),
    path('productos/buscar/', views.buscar_productos, name='buscar_productos'),
    
    # Categorías
    path('categorias/', views.CategoriaListView.as_view(), name='lista_categorias'),
    path('categorias/crear/', views.CategoriaCreateView.as_view(), name='crear_categoria'),
    path('categorias/<int:pk>/editar/', views.CategoriaUpdateView.as_view(), name='editar_categoria'),
    path('categorias/<int:id>/eliminar/', views.eliminar_categoria, name='eliminar_categoria'),
    path('categorias/<int:pk>/productos/', views.CategoriaProductosListView.as_view(), name='categoria_productos'),

    # Etiquetas
    path('etiquetas/', views.EtiquetaListView.as_view(), name='lista_etiquetas'),
    path('etiquetas/crear/', views.EtiquetaCreateView.as_view(), name='crear_etiqueta'),
    path('etiquetas/<int:pk>/editar/', views.EtiquetaUpdateView.as_view(), name='editar_etiqueta'),
    path('etiquetas/<int:id>/eliminar/', views.eliminar_etiqueta, name='eliminar_etiqueta'),
]