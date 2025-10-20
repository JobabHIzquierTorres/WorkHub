# 🧭 WorkHub – Plataforma SaaS para comunicación interna y gestión del empleado

**WorkHub** es una plataforma SaaS diseñada para optimizar la comunicación interna y la gestión del empleado dentro de una organización.  
Desarrollada sobre la arquitectura escalable de Django, permite integrar nuevas funcionalidades de forma modular y adaptable a las necesidades de cada empresa.

![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Django](https://img.shields.io/badge/Django-Backend-green.svg)
![Status](https://img.shields.io/badge/Status-En%20desarrollo-yellow.svg)

---

## 📚 Índice
- [Características](#-características-principales)
- [Tecnologías utilizadas](#-tecnologías-utilizadas)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [Instalación y uso](#-instalación-y-uso)
- [Estado del proyecto](#-estado-del-proyecto)
- [Licencia](#-licencia--creative-commons-attribution-noncommercial-40-international-cc-by-nc-40)
- [Contribuciones](#-contribuciones)
- [Contacto](#-contacto)

---

## 🚀 Características principales

- 📰 **Noticias internas**: Los empleados registrados pueden acceder a las noticias y novedades de la empresa.  
- 👤 **Gestión de perfil**: Cada usuario puede actualizar su información personal, cambiar su contraseña y su email.  
- 📅 **Calendario personal**: Cada empleado cuenta con un calendario individual para organizar sus eventos y tareas.  
- 💬 **Chat interno sin WebSocket**: Comunicación sencilla y concreta entre empleados, evitando distracciones innecesarias.  
- 🛡️ **Gestión de roles**:
  - Solo el **administrador** puede crear, modificar y eliminar noticias.
  - Los empleados tienen permisos limitados según su rol asignado.
- 🧱 **Escalabilidad**: Gracias a la estructura de Django, se pueden añadir nuevas funcionalidades o adaptar las existentes con facilidad.

---

## 🛠️ Tecnologías utilizadas

- [Django](https://www.djangoproject.com/) – Backend escalable y seguro.  
- [SQLite / PostgreSQL] – Base de datos adaptable.  
- HTML5 / CSS3 / JS – Interfaz básica y funcional.  
- Python 3.x – Lenguaje base del proyecto.

---

## 🏗️ Estructura del proyecto

```
WorkHub/
├── core/                # Configuración principal de Django
├── profiles/            # Gestión de usuarios, perfiles y roles
├── notices/             # Módulo de noticias internas
├── messenger/           # Chat sin WebSocket
├── userCalendar/        # Calendario personal de empleados
├── registration/        # Gestión de registros de nuevos usuarios y cambios de contraseña o email
├── sent_emails/         # Recoge los emails enviados para recuperar contraseña
├── requirements.txt     # Dependencias          
├── db.sqlite3         
└── manage.py
```
---

## ⚡ Instalación y uso

1. **Clonar el repositorio**  
   ```bash
   git clone https://github.com/JobabHIzquierTorres/WorkHub.git
   cd workhub
   cd app_mensajeria

2. **Crear y activar entorno virtual**
   ```bash
   python -m venv env
   source env/bin/activate   # Linux/Mac
   env\Scripts\activate      # Windows
   
3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   
4. **Realizar migraciones e iniciar el servidor**
   ```bash
   python manage.py migrate
   python manage.py runserver
   
5. **Acceder a la aplicación**
    👉 http://127.0.0.1:8000/

---

## 🧭 Objetivo del proyecto
WorkHub busca ser una herramienta eficiente para mejorar la comunicación interna,
reducir distracciones y facilitar la gestión de empleados, manteniendo una estructura
limpia y escalable para futuras ampliaciones.

---
## 🚧 Estado del Proyecto
**Importante:** Este backend se encuentra actualmente en **fase de desarrollo** y no está preparado para despliegue en producción. 
### Limitaciones actuales:
- Configuración de seguridad básica, no optimizada para entornos productivos.
- Falta de configuración para despliegue (servidores, base de datos, etc.).
- Puede contener funcionalidades incompletas o errores.
### Recomendaciones:
- Utilizar únicamente en entornos de desarrollo y testing.
- No utilizar en producción hasta completar las configuraciones de seguridad y despliegue.
---

# 📄 Licencia – Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)

Este proyecto de backend ha sido desarrollado por **Jobab Hacomar Izquier Torres** y se encuentra bajo la licencia **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**.

## ✅ Permisos otorgados

Puedes:

- **Compartir**: copiar y redistribuir el material en cualquier medio o formato.
- **Adaptar**: remezclar, transformar y construir a partir del material.

Siempre que:

- Se dé **crédito adecuado** al autor original.
- Se incluya un enlace a esta licencia.
- Se indique si se han realizado cambios.

## ❌ Restricciones

No puedes:

- Usar el material con **fines comerciales**.
- Aplicar restricciones legales o tecnológicas que impidan a otros hacer lo que permite esta licencia.

## 📌 Atribución

Ejemplo recomendado de atribución:

> Backend desarrollado por **Jobab Hacomar Izquier Torres** – Licencia CC BY-NC 4.0  
> [https://creativecommons.org/licenses/by-nc/4.0/](https://creativecommons.org/licenses/by-nc/4.0/)

## 🔗 Enlace oficial

Consulta los términos completos de la licencia en el sitio oficial de Creative Commons:  
👉 [https://creativecommons.org/licenses/by-nc/4.0/](https://creativecommons.org/licenses/by-nc/4.0/)

---

## 🛡️ Garantía

Este software se proporciona "tal cual", sin garantías de ningún tipo.
El autor no se hace responsable de posibles daños derivados del uso del código.

---

## ⭐ Contribuciones

Las contribuciones son bienvenidas siempre que respeten la licencia.  
Si deseas colaborar:

1. Haz un **fork** del repositorio.  
2. Crea una **rama** para tu mejora o corrección.  
3. Realiza un **pull request** con una descripción clara de los cambios.

---

## 📬 Contacto

📧 [jhizquier.dev@gmail.com](mailto:jhizquier.dev@gmail.com)  

🌐 [Creative Commons — Licencia CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)

---
