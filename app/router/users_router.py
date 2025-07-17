from fastapi import APIRouter, HTTPException, Query, Body
from typing import List

from app.services import userService

from app.schemas.users_shema import (
    UserResponseSchema,
    UserCreateSchema,
)
from app.schemas.base_shema import BaseFilterShema

router = APIRouter(prefix="/users", tags=["users"])


@router.get(
    "/all",
    response_model=List[UserResponseSchema],
    summary="API para obtener todos los usuarios",
)
async def get_user_all():
    return await userService.get_user_all()


@router.post(
    "/by-filter",
    response_model=List[UserResponseSchema],
    summary="API para obtener usuarios por filtro",
)
async def get_users_by_filter(
    filtros: BaseFilterShema = Body(..., description="Filtros para buscar usuarios")
):
    return await userService.get_users_by_filter(filtros)


@router.get(
    "/by-email",
    response_model=UserResponseSchema,
    summary="API para obtener usuario por email",
)
async def get_user_by_email(
    email: str = Query(..., description="Correo electrónico del usuario")
):
    return await userService.get_user_by_email(email)


@router.post(
    "/crear",
    response_model=UserResponseSchema,
    summary="API para crear un nuevo usuario",
)
async def post_user_create(
    usuario: UserCreateSchema = Body(
        ..., description="Datos necesarios para crear un nuevo usuario"
    )
):
    return await userService.post_user_create(usuario)
