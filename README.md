# Demo OAuth2 con Google

Este proyecto es una prueba de concepto de autenticación con Google OAuth2 usando un frontend en HTML/JS y un backend en FastAPI.

## 1. Clonar el repositorio

```bash
https://github.com/10santiago12/Ejemplo-Microservicios.git
cd Ejemplo-Microservicios
```

## 2. Crear y activar entorno virtual (opcional)

### En Windows (PowerShell):

```bash
python -m venv venv
.\venv\Scripts\activate
```

### En Linux/Mac:

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Instalar dependencias

```bash
pip install fastapi uvicorn python-jose google-auth
```

## 4. Iniciar el backend (FastAPI)

```bash
uvicorn main:app --reload --port 5000

```
## 5. (Opcional) En caso de fallo, instalar requests para que no falten dependencias.

```bash
pip install requests

```

El backend estará disponible en: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## 5. Iniciar el frontend (HTML/JS)

En la carpeta del proyecto, levanta un servidor local con:

```bash
python -m http.server 8000
```

El frontend estará disponible en: [http://localhost:8000](http://localhost:8000)

## 6. Probar la autenticación

1. Abre el frontend en el navegador.
2. Haz clic en el botón de **Google Login**.
3. Selecciona una cuenta de Google.
4. El backend validará el token y mostrará la información del usuario.

## Notas importantes

En la configuración del cliente OAuth2 de Google, los orígenes autorizados deben incluir:

- [http://localhost:8000](http://localhost:8000)
- [http://127.0.0.1:5000](http://127.0.0.1:5000)
