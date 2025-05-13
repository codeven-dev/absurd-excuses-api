
# 📘 API de Excusas sin sentido

Una simple API REST creada con FastAPI que devuelve excusas aleatorias, absurdas y graciosas. Ideal como primer proyecto para aprender sobre desarrollo backend, rutas HTTP y entornos virtuales en Python.

## 🚀 ¿Qué hace esta API?

Esta API responde con excusas tontas y sin sentido, perfectas para divertirte, romper el hielo o justificar tu falta de productividad con estilo.

**Endpoints disponibles:**

```
GET /
Muestra un mensaje de bienvenida.
```
```
GET /excusas
Devuelve una lista completa de excusas disponibles.
```
```
GET /excusas/random
Devuelve una excusa aleatoria.
```

## 📂 Estructura del Proyecto

```javascript
frases-api/
│
├── excusas.json           # Archivo con excusas
├── main.py                # Código principal de la API
└── requirements.txt       # Dependencias del entorno
```

## 🛠️ Tecnologías Usadas
● Python 3.11

● FastAPI

● Uvicorn

## 🔧 Instalación y Uso

Clona el repositorio:

```bash
 git clone https://github.com/codeven-dev/absurd-excuses-api.git
 cd absurd-excuses-api
```

Instala las dependencias:

```bash
 pip install -r requirements.txt
```

Corre el servidor:

```bash
 uvicorn main:app --reload
```

**Accede a la API en:** http://localhost:8000
