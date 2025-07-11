from fastapi import FastAPI
from app.router import users
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="fluxnet API",
    description="API desarrollado con FastAPI, para ser consumida entre fluxnet y servicios externos",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users)  
