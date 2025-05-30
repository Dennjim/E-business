
# Ferreteria E-commerce Project

This is a basic e-commerce application built with Django, simulating a hardware store (ferretería) where users can browse products, add them to a shopping cart, and place orders.

## Features

* **Product Catalog:** Displays a list of available hardware products with images, names, categories, and prices.
* **Shopping Cart:** Users can add products to a cart, adjust quantities, and remove items.
* **Order Placement:** A "Colocar Pedido" (Place Order) button finalizes the order, saving it to the database with a "pendiente" (pending) status and emptying the cart.
* **Basic UI/UX:** Improved user interface for a cleaner and more intuitive Browse and shopping experience.
* **Static and Media File Handling:** Configured to serve static assets (CSS) and user-uploaded media (product images).

## Technologies Used

* **Django:** Web framework for the backend logic.
* **Python:** Programming language.
* **SQLite:** Default database for development.
* **HTML/CSS:** For the front-end structure and styling.
* **Font Awesome:** For icons (e.g., shopping cart icon).

## Setup and Installation

Follow these steps to get the project up and running on your local machine.

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd ferreteria_project
```
*(Replace `<your-repository-url>` with the actual URL of your GitHub repository)*

### 2. Create a Virtual Environment

It's highly recommended to use a virtual environment to manage project dependencies.

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

* **Windows:**
    ```bash
    .\venv\Scripts\activate
    ```
* **macOS/Linux:**
    ```bash
    source venv/bin/activate
    ```

### 4. Install Dependencies

You'll need to install Django and any other libraries your project uses. If you have a `requirements.txt` (recommended for larger projects, but for now we'll assume just Django), you'd use that.

```bash
pip install Django pillow # Pillow is needed for image handling
```

### 5. Database Migrations

Apply the database migrations to create the necessary tables.

```bash
python manage.py makemigrations tienda_app
python manage.py migrate
```

### 6. Create a Superuser (Optional but Recommended)

This allows you to access the Django admin panel to manage products, categories, etc.

```bash
python manage.py createsuperuser
```
Follow the prompts to create your username, email, and password.

### 7. Run the Development Server

```bash
python manage.py runserver
```

### 8. Access the Application

Open your web browser and go to:

* **Product Catalog:** `http://127.0.0.1:8000/`
* **Django Admin:** `http://127.0.0.1:8000/admin/`

## Project Structure

```
ferreteria_project/
├── ferreteria_project/  # Main project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tienda_app/          # Core e-commerce application
│   ├── migrations/
│   ├── static/          # For app-specific static files (e.g., CSS for this app)
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
├── media/               # Directory for user-uploaded files (e.g., product images)
├── venv/                # Python Virtual Environment (ignored by Git)
├── manage.py
└── README.md
└── .gitignore
```

## Contributing

Feel free to fork the repository, make improvements, and submit pull requests!

## License

[Specify your license here, e.g., MIT, Apache 2.0, etc. If no license, state "No license specified." For a basic project, MIT is a common choice.]
```







