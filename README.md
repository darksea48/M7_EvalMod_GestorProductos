# 🛒 Gestor de Productos - Sistema de Inventario Django

[![Django](https://img.shields.io/badge/Django-5.2.7-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0-orange.svg)](https://www.mysql.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.3-purple.svg)](https://getbootstrap.com/)

Un sistema completo de gestión de productos desarrollado con Django y MySQL, que incluye funcionalidades CRUD, búsqueda avanzada, relaciones entre modelos y una interfaz de usuario moderna y responsive.

## 📋 Tabla de Contenidos

- [Características](#-características)
- [Tecnologías Utilizadas](#-tecnologías-utilizadas)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Instalación y Configuración](#-instalación-y-configuración)
- [Uso del Sistema](#-uso-del-sistema)
- [Modelos de Datos](#-modelos-de-datos)
- [API y Vistas](#-api-y-vistas)
- [Funcionalidades Destacadas](#-funcionalidades-destacadas)
- [Capturas de Pantalla](#-capturas-de-pantalla)
- [Contribución](#-contribución)
- [Licencia](#-licencia)

## ✨ Características

### 🔧 Funcionalidades Principales
- **CRUD Completo**: Crear, leer, actualizar y eliminar productos, categorías y etiquetas
- **Búsqueda Avanzada**: Búsqueda inteligente en múltiples campos (nombre, descripción, categoría, etiquetas)
- **Relaciones de Datos**: Implementación de relaciones OneToOne, ForeignKey y ManyToMany
- **Interfaz Responsive**: Diseño adaptativo para dispositivos móviles y escritorio
- **Administración Django**: Panel de administración personalizado con inlines
- **Validaciones**: Validación tanto del lado cliente como del servidor
- **Mensajes Flash**: Notificaciones user-friendly con SweetAlert2

### 🎨 Características de UX/UI
- **Diseño Moderno**: Interfaz limpia con Bootstrap 5.3.3
- **Iconografía**: Bootstrap Icons para mejor experiencia visual
- **Confirmaciones**: Diálogos de confirmación para acciones destructivas
- **Feedback Visual**: Badges, alertas y mensajes informativos
- **Navegación Intuitiva**: Estructura de navegación clara y consistente

## 🛠 Tecnologías Utilizadas

### Backend
- **Django 5.2.7**: Framework web de Python
- **MySQL**: Base de datos relacional
- **Python 3.13**: Lenguaje de programación

### Frontend
- **Bootstrap 5.3.3**: Framework CSS para diseño responsive
- **Bootstrap Icons 1.11.3**: Iconografía
- **jQuery 3.7.1**: Biblioteca JavaScript
- **SweetAlert2**: Diálogos y alertas modernas

### Herramientas de Desarrollo
- **Django ORM**: Mapeo objeto-relacional
- **Django Admin**: Panel de administración
- **Django Forms**: Validación y renderizado de formularios
- **Django Messages**: Sistema de mensajes flash

## 📁 Estructura del Proyecto

```
eval_mod_m7/
├── 📄 manage.py                    # Script de gestión de Django
├── 📄 README.md                    # Documentación del proyecto
├── 📁 ProyGestorProductos/         # Configuración del proyecto
│   ├── 📄 __init__.py
│   ├── 📄 settings.py              # Configuraciones de Django
│   ├── 📄 urls.py                  # URLs principales
│   ├── 📄 wsgi.py                  # Configuración WSGI
│   └── 📄 asgi.py                  # Configuración ASGI
├── 📁 app_productos/               # Aplicación principal
│   ├── 📄 models.py                # Modelos de datos
│   ├── 📄 views.py                 # Vistas de la aplicación
│   ├── 📄 urls.py                  # URLs de la aplicación
│   ├── 📄 forms.py                 # Formularios Django
│   ├── 📄 admin.py                 # Configuración del admin
│   ├── 📄 apps.py                  # Configuración de la app
│   ├── 📁 migrations/              # Migraciones de base de datos
│   └── 📁 templates/               # Templates HTML
│       ├── 📄 list.html            # Lista de elementos
│       ├── 📄 form.html            # Formularios
│       ├── 📄 detail.html          # Detalle de elementos
│       └── 📄 confirmar_eliminacion.html
├── 📁 templates/                   # Templates globales
│   ├── 📄 base.html                # Template base
│   └── 📄 index.html               # Página de inicio
└── 📁 static/                      # Archivos estáticos
    └── 📁 css/
        └── 📄 styles.css           # Estilos personalizados
```

## 🚀 Instalación y Configuración

### Prerrequisitos
- Python 3.13+
- MySQL 8.0+
- pip (gestor de paquetes de Python)

### 1. Clonar el Repositorio
```bash
git clone https://github.com/darksea48/M7_AE6_AEPRO_ONG.git
cd eval_mod_m7
```

### 2. Crear Entorno Virtual
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependencias
```bash
pip install django==5.2.7
pip install mysqlclient
```

### 4. Configurar Base de Datos MySQL

#### Crear base de datos:
```sql
CREATE DATABASE gestorproductos CHARACTER SET utf8  DEFAULT COLLATE utf8_general_ci;
```

#### Configurar settings.py (si es necesario):
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gestorproductos',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5. Ejecutar Migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Crear Superusuario
```bash
python manage.py createsuperuser
```

### 7. Ejecutar Servidor de Desarrollo
```bash
python manage.py runserver
```

La aplicación estará disponible en: `http://127.0.0.1:8000/`

## 🎯 Uso del Sistema

### Acceso a la Aplicación
- **Página Principal**: `http://127.0.0.1:8000/`
- **Lista de Productos**: `http://127.0.0.1:8000/productos/`
- **Panel de Admin**: `http://127.0.0.1:8000/admin/`

### Navegación Principal
1. **Productos**: Gestionar inventario de productos
2. **Categorías**: Organizar productos por categorías
3. **Etiquetas**: Sistema de etiquetado flexible
4. **Búsqueda**: Búsqueda avanzada en múltiples campos (nombre, descripción, categoría, etiquetas)

### Funcionalidades por Módulo

#### 📦 Gestión de Productos
- ✅ Crear nuevo producto con detalles físicos
- ✅ Listar productos con información resumida
- ✅ Ver detalles completos de un producto
- ✅ Editar información de productos existentes
- ✅ Eliminar productos con confirmación
- ✅ Buscar productos por múltiples criterios

#### 📂 Gestión de Categorías
- ✅ Crear y organizar categorías
- ✅ Ver conteo de productos por categoría
- ✅ Editar información de categorías
- ✅ Eliminar categorías (con validación de dependencias)

#### 🏷️ Gestión de Etiquetas
- ✅ Sistema flexible de etiquetado
- ✅ Relación muchos-a-muchos con productos
- ✅ Conteo de productos por etiqueta
- ✅ Gestión completa CRUD

## 🗄️ Modelos de Datos

### Producto
```python
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    etiquetas = models.ManyToManyField(Etiqueta, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
```

### Categoría
```python
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
```

### Etiqueta
```python
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
```

### DetalleProducto (Relación OneToOne)
```python
class DetalleProducto(models.Model):
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE, primary_key=True)
    peso = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    ancho = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    alto = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    largo = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
```

### Relaciones Implementadas
- **Uno a Uno (1:1)** con el campo **OneToOneField**: Producto ↔ DetalleProducto
- **Uno a Muchos (1:N)** con el campo **ForeignKey**: Producto → Categoría (Many-to-One)
- **Muchos a Muchos (N:M)** con el campo **ManyToManyField**: Producto ↔ Etiqueta

## 🔧 API y Vistas

### Vistas Principales

#### Vistas Basadas en Clases (CBV)
- `ProductoListView`: Lista de productos con paginación
- `ProductoCreateView`: Creación de productos
- `ProductoUpdateView`: Edición de productos
- `ProductoDetailView`: Detalle de producto
- `CategoriaListView`: Lista de categorías con conteo
- `EtiquetaListView`: Lista de etiquetas con conteo
- `CategoriaProductosListView`: Lista de productos por categoría
- `EtiquetaProductosListView`: Lista de productos por etiqueta

#### Vistas Basadas en Funciones (FBV)
- `buscar_productos`: Búsqueda avanzada con Q objects
- `eliminar_producto`: Eliminación con confirmación
- `eliminar_categoria`: Eliminación de categorías
- `eliminar_etiqueta`: Eliminación de etiquetas

### URLs Pattern
```python
urlpatterns = [
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
    path('etiquetas/<int:pk>/productos/', views.EtiquetaProductosListView.as_view(), name='etiqueta_productos'),
]
```

## 🌟 Funcionalidades Destacadas

### 🔍 Búsqueda Avanzada
- **Múltiples campos**: Busca en nombre, descripción, categoría y etiquetas
- **Búsqueda insensible**: No distingue mayúsculas/minúsculas
- **Coincidencias parciales**: Encuentra términos dentro de palabras
- **Sin duplicados**: Usa `distinct()` para evitar repeticiones
- **Feedback visual**: Muestra cantidad de resultados encontrados

```python
# Implementación de búsqueda
productos_encontrados = Producto.objects.filter(
    Q(nombre__icontains=query) |
    Q(descripcion__icontains=query) |
    Q(categoria__nombre__icontains=query) |
    Q(etiquetas__nombre__icontains=query)
).distinct()
```

### 📊 Contadores Dinámicos
- **Productos por categoría**: Usando `annotate()` y `Count()`
- **Productos por etiqueta**: Optimización de consultas SQL
- **Badges visuales**: Indicadores coloridos según la cantidad

```python
# Optimización con annotate
categorias_con_conteo = Categoria.objects.annotate(
    total_productos=Count('productos')
).order_by('nombre')
```

### 🔗 Formularios Unificados
- **Producto + DetalleProducto**: Un solo formulario para ambos modelos
- **Validación personalizada**: Lógica de negocio en el formulario
- **Manejo de relaciones**: Gestión automática de OneToOne

### 🎨 Experiencia de Usuario
- **SweetAlert2**: Confirmaciones elegantes para eliminaciones
- **Bootstrap 5**: Diseño moderno y responsive
- **Mensajes Flash**: Feedback inmediato de acciones
- **Navegación intuitiva**: Estructura clara y consistente

## 📸 Capturas de Pantalla

### Página Principal
- Dashboard con acceso rápido a todas las funcionalidades
- Navegación clara y organizada
- Enlaces directos a crear elementos

### Lista de Productos
- Vista de tarjetas responsive
- Información resumida de cada producto
- Botones de acción (Ver, Editar, Eliminar)
- Barra de búsqueda integrada

### Formulario de Producto
- Campos unificados para Producto y DetalleProducto
- Validación en tiempo real
- Selección de categoría y etiquetas
- Diseño responsive y accessible

### Panel de Administración
- Admin de Django personalizado
- Inlines para DetalleProducto
- Filtros y búsquedas optimizadas
- Gestión completa de relaciones

## 🤝 Contribución

### Cómo Contribuir
1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -m 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

### Estándares de Código
- Seguir PEP 8 para Python
- Documentar funciones y clases
- Escribir tests para nuevas funcionalidades
- Mantener cobertura de tests

### Reportar Bugs
- Usar el sistema de Issues de GitHub
- Incluir pasos para reproducir el bug
- Especificar versiones de Python y Django
- Adjuntar capturas de pantalla si es necesario

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

## 👨‍💻 Autor

**Douglas Suárez Zamorano**
- GitHub: [@darksea48](https://github.com/darksea48)
- Email: d.suarez.zamorano@gmail.com

## 🙏 Agradecimientos

- **Cynthia Castillo y Ricardo Vega**: Mis profesores del Bootcamp de Python/Django
- **Valeria Jara Bugueño**: Mi amada esposa que me ha estado acompañando en todo este trayecto en este curso
- **Cristian Astudillo y Gerard Bourguett**: Mis grandes amigos que me han apoyado en todo
- **Joaquín González**: Mi compañero de trabajo que me ha acompañado en todo este curso con buenos tips de Python

---

### Documentación Adicional
- [Documentación de Django](https://docs.djangoproject.com/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)
- [MySQL Documentation](https://dev.mysql.com/doc/)

⭐ Si este proyecto te ha sido útil, ¡considera darle una estrella en GitHub!

📚 **Proyecto desarrollado como parte del Bootcamp Full Stack Python/Django**