from passlib.context import CryptContext
from fastapi import HTTPException

from app.dtos import UserCreateDTO, UserUpdateDTO, BaseAuditDTO, BaseFilterDTO

# from app.repository import (
#     get_user_all,
#     get_user_by_filter,
#     get_user_by_email,
#     post_user_create,
# )
from app.repository import userRepository


from app.schemas import BaseAuditSchema, User, UserResponse


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# gets
def get_user_all() -> UserResponse:
    user_data = userRepository.get_user_all()
    if not user_data:
        raise HTTPException(status_code=404, detail="Sin Usuarios")
    return UserResponse(**user_data)


def get_users_by_filter(filters: BaseFilterDTO) -> list[UserResponse]:
    user_rows = userRepository.get_user_by_filter(filters)
    return [UserResponse(**row) for row in user_rows]


def get_user_by_email(email: str) -> UserResponse:
    user_data = userRepository.get_user_by_email(email)
    if not user_data:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return UserResponse(**user_data)


# post
def post_user_create(userCreateDTO: UserCreateDTO) -> list[UserResponse]:
    user_rows = userRepository.post_user_create(userCreateDTO)
    return [UserResponse(**row) for row in user_rows]


class UserService:
    get_user_all = staticmethod(get_user_all)
    get_user_by_email = staticmethod(get_user_by_email)
    get_users_by_filter = staticmethod(get_users_by_filter)
    post_user_create = staticmethod(post_user_create)


userService = UserService()
