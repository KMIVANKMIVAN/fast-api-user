from fastapi import APIRouter, HTTPException, Query, Body

from typing import List

from app.services import userService

from app.schemas.users_shema import UserResponse

from app.dtos.base_dto import BaseFilterDTO
from app.dtos.user_dto import UserUpdateDTO, UserCreateDTO

router = APIRouter(prefix="/users", tags=["users"])


@router.get(
    "/all",
    response_model=List[UserResponse],
    summary="API para obtener todos los usuario",
)
def get_user_all():
    return userService.get_user_all()


@router.get(
    "/by-filter",
    response_model=List[UserResponse],
    summary="API para obtener usuarios por el filtro",
)
def get_users_by_filter(baseFilterDTO: BaseFilterDTO):
    return userService.get_users_by_filter(baseFilterDTO)


@router.get(
    "/by-email",
    response_model=UserResponse,
    summary="API para obtener usuario por email",
)
def get_user_by_email(
    email: str = Query(..., description="Correo electrónico del usuario")
):
    return userService.get_user_by_email(email)


@router.post(
    "/crear",
    response_model=UserResponse,
    summary="API para crear un nuevo Usuario",
)
def crear_parametro(
    parametro: UserCreateDTO = Body(
        ...,
        description="Esta API permite crear un nuevo Usuario utilizando los datos proporcionados en el cuerpo de la solicitud.",
    )
):
    return userService.post_user_create(parametro)
