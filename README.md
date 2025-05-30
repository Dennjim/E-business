

# Proyecto de E-commerce: Ferretería

Esta es una aplicación básica de e-commerce construida con Django, que simula una ferretería donde los usuarios pueden explorar productos, añadirlos a un carrito de compras y realizar pedidos.

---

## Características

* **Catálogo de Productos:** Muestra una lista de productos de ferretería disponibles con imágenes, nombres, categorías y precios.
* **Carrito de Compras:** Los usuarios pueden añadir productos al carrito, ajustar cantidades y eliminar artículos.
* **Realización de Pedidos:** Un botón "Colocar Pedido" finaliza la orden, guardándola en la base de datos con un estado "pendiente" y vaciando el carrito.
* **UI/UX Básica:** Interfaz de usuario mejorada para una experiencia de navegación y compra más limpia e intuitiva.
* **Manejo de Archivos Estáticos y Multimedia:** Configurado para servir activos estáticos (CSS) y contenido multimedia subido por el usuario (imágenes de productos).

---

## Tecnologías Utilizadas

* **Django:** Framework web para la lógica del backend.
* **Python:** Lenguaje de programación.
* **SQLite:** Base de datos predeterminada para desarrollo.
* **HTML/CSS:** Para la estructura y el estilo del frontend.
* **Font Awesome:** Para íconos (por ejemplo, el ícono del carrito de compras).

---

## Configuración e Instalación

Sigue estos pasos para poner el proyecto en funcionamiento en tu máquina local.

### 1. Clonar el Repositorio

```bash
git clone https://github.com/Dennjim/E-business.git
cd E-business
```

### 2. Crear un Entorno Virtual

Es altamente recomendable usar un entorno virtual para gestionar las dependencias del proyecto.

```bash
python -m venv venv
```

### 3. Activar el Entorno Virtual

* **Windows:**
    ```bash
    .\venv\Scripts\activate
    ```
* **macOS/Linux:**
    ```bash
    source venv/bin/activate
    ```

### 4. Instalar Dependencias

Necesitarás instalar Django y cualquier otra librería que use tu proyecto.

```bash
pip install Django pillow # Pillow es necesario para el manejo de imágenes
```

### 5. Migraciones de la Base de Datos

Aplica las migraciones de la base de datos para crear las tablas necesarias.

```bash
python manage.py makemigrations tienda_app
python manage.py migrate
```

### 6. Crear un Superusuario (Opcional pero Recomendado)

Esto te permite acceder al panel de administración de Django para gestionar productos, categorías, etc.

```bash
python manage.py createsuperuser
```

Sigue las indicaciones para crear tu nombre de usuario, correo electrónico y contraseña.

### 7. Ejecutar el Servidor de Desarrollo

```bash
python manage.py runserver
```

### 8. Acceder a la Aplicación

Abre tu navegador web y ve a:

* **Catálogo de Productos:** `http://127.0.0.1:8000/`
* **Panel de Administración de Django:** `http://127.0.0.1:8000/admin/`

---

## Estructura del Proyecto

```
ferreteria_project/
├── ferreteria_project/  # Configuración principal del proyecto
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tienda_app/          # Aplicación principal de e-commerce
│   ├── migrations/
│   ├── static/          # Para archivos estáticos específicos de la aplicación (ej. CSS)
│   ├── templates/
│   │   └── tienda_app/
│   │       ├── catalogo.html
│   │       ├── carrito.html
│   │       ├── pedido_exitoso.html
│   │       └── carrito_vacio.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── media/               # Directorio para archivos subidos por el usuario (ej. imágenes de productos)
├── venv/                # Entorno Virtual de Python (ignorado por Git)
├── manage.py
└── README.md
└── .gitignore
```

---

## Contribuciones

¡No dudes en hacer un "fork" del repositorio, realizar mejoras y enviar solicitudes de extracción ("pull requests")!

---

