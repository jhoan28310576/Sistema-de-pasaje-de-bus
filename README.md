Sistema de Gestión de Pasajes de Autobús
Descripción del Proyecto
Este es un sistema completo de gestión de pasajes de autobús desarrollado con Django que permite a los usuarios comprar pasajes y a los administradores gestionar la oferta de viajes.

🚍 Características Principales
Para Usuarios
Registro y Autenticación segura de usuarios

Recarga de Saldo electrónico

Compra de Pasajes con validación de disponibilidad

Visualización de Saldo disponible

Generación de Tickets digitales al comprar

![Screenshot_1](https://github.com/user-attachments/assets/52668d6f-21ca-48b5-af89-3ee5f07cf49b)

![Screenshot_2](https://github.com/user-attachments/assets/15a864ec-5dcd-4703-a30f-170bea7d4e0a)

![Screenshot_3](https://github.com/user-attachments/assets/4f0f7d1e-10b4-4fbd-b5b1-9f05a18b1221)

![menu narbar](https://github.com/user-attachments/assets/d5004eb3-4c1e-4c70-bc46-5f1ff32a79d3)

Para Administradores
Gestión CRUD de pasajes:

Agregar nuevos viajes/rutas

Modificar detalles existentes

Eliminar pasajes

Control de Inventario: Cantidad disponible de pasajes

Visualización de Capital total de la agencia

![adminsecion](https://github.com/user-attachments/assets/870df4e4-c42e-4acf-8f18-037798eaacac)

![agregar pasahe](https://github.com/user-attachments/assets/87c82ffa-fba9-4b43-90ce-7bd29927a6ab)

![modificaroassje](https://github.com/user-attachments/assets/82398bdc-8a6f-4eef-a098-f21749cbec3f)

![eliminar passje](https://github.com/user-attachments/assets/1fcff8b7-44e3-4d33-ab7d-3697505e7513)

![recargasaldo](https://github.com/user-attachments/assets/d287e53c-1240-4c9b-b62b-c637d19b8daa)

🛠️ Estructura Técnica
Modelos de Datos
PerfilUsuario:

Relación 1:1 con User de Django

saldo_total: Saldo disponible del usuario

AgenciaPasaje:

nombre: Nombre del pasaje/ruta

precio: Costo del pasaje

saldo_total: Capital de la agencia

cantidad_disponible: Pasajes en stock

Vistas Principales
Autenticación: Registro y login con protección contra fuerza bruta

Menú Principal: Listado paginado de pasajes con búsqueda

Transacciones:

Recarga de saldo

Compra de pasajes (con actualización automática de saldos)

Gestión Admin:

CRUD completo de pasajes

Visualización de capital total

📊 Flujo de Transacciones
Usuario recarga saldo → aumenta PerfilUsuario.saldo_total

Usuario compra pasaje:

Verifica saldo suficiente y disponibilidad

Actualiza saldos (usuario y agencia)

Reduce cantidad disponible

Genera ticket digital

🚀 Cómo Empezar
Clonar el repositorio

Instalar dependencias: pip install -r requirements.txt

Ejecutar migraciones: python manage.py migrate

Crear superusuario: python manage.py createsuperuser

Iniciar servidor: python manage.py runserver

📌 Requisitos
Python 3.8+

Django 4.0+

PostgreSQL (recomendado) o SQLite

📝 Licencia
Este proyecto está bajo licencia MIT.

markdown
## Estructura de Archivos
app-pasajes/
├── migrations/ # Migraciones de la base de datos
├── templates/ # Plantillas HTML
│ ├── inicio/ # Autenticación y recargas
│ └── app-pasaje/ # Vistas principales
├── init.py
├── admin.py # Configuración del admin
├── apps.py
├── forms.py # Formularios personalizados
├── models.py # Modelos de datos
├── tests.py
├── urls.py # Rutas de la aplicación
└── views.py # Lógica de vistas


## Roadmap
- [ ] Integración con pasarelas de pago
- [ ] Historial de transacciones
- [ ] API REST para móviles
- [ ] Sistema de reservas

---

Esta descripción:
1. Presenta claramente las funcionalidades
2. Explica la estructura técnica
3. Incluye instrucciones básicas de instalación
4. Muestra la organización del código
5. Sugiere mejoras futuras

