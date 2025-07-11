from passlib.context import CryptContext
from fastapi import HTTPException
from app.repository.users_repository import get_user_by_email, get_user_by_filter, get_user_all
from app.schemas.users_shema import UserResponse

from app.dtos import UserCreateDTO, BaseFilterDTO


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def service_get_user_all() -> UserResponse:
    user_data = get_user_all()
    if not user_data:
        raise HTTPException(status_code=404, detail="Sin Usuarios")
    return UserResponse(**user_data)

def service_get_user_by_email(email: str) -> UserResponse:
    user_data = get_user_by_email(email)
    if not user_data:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return UserResponse(**user_data)


def service_get_users_by_filter(filters: BaseFilterDTO) -> list[UserResponse]:
    user_rows = get_user_by_filter(filters)
    return [UserResponse(**row) for row in user_rows]

  