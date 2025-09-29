from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer
from google.oauth2 import id_token
from google.auth.transport import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
auth_scheme = HTTPBearer()

origins = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

GOOGLE_CLIENT_ID = "440257891541-faoulq5g61v2efoen1qj5mk0fa2r7jnm.apps.googleusercontent.com"

def verify_google_token(credentials=Depends(auth_scheme)):
    token = credentials.credentials
    try:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), GOOGLE_CLIENT_ID)
        return idinfo
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado",
        )

@app.get("/perfil")
def perfil(user=Depends(verify_google_token)):
    return {
        "mensaje": f"Bienvenido {user['name']}",
        "email": user["email"],
        "foto": user.get("picture")
    }
