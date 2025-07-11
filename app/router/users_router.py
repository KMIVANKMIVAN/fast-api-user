from fastapi import APIRouter, HTTPException, Query
from typing import List
from app.services.users_service import (
    service_get_user_all,
    service_get_user_by_email,
    service_get_users_by_filter
)

from app.schemas.users_shema import UserResponse

from app.dtos.base_dto import BaseFilterDTO

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/all", response_model=List[UserResponse])
def get_all_users():
    return service_get_user_all()


@router.get("/by-email", response_model=UserResponse)
def get_user_by_email(email: str = Query(..., description="Correo electrónico del usuario")):
    return service_get_user_by_email(email)


@router.post("/filter", response_model=List[UserResponse])
def get_users_by_filter(filters: BaseFilterDTO):
    return service_get_users_by_filter(filters)
