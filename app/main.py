from fastapi import FastAPI
from app.router import users
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import create_db_and_tables
import app.model

app = FastAPI(
    title="fluxnet API",
    description="API desarrollado con FastAPI, para ser consumida entre fluxnet y servicios externos",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(users)
app.include_router(users, prefix="/api")


# Este bloque se ejecuta al iniciar la app
@app.on_event("startup")
async def on_startup():
    await create_db_and_tables()
