from fastapi import HTTPException
from passlib.context import CryptContext
from app.repository import userRepository
from app.schemas import UserResponseSchema, BaseFilterShema, UserCreateSchema

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def get_user_all() -> UserResponseSchema:
    user_data = await userRepository.get_user_all()
    if not user_data:
        raise HTTPException(status_code=404, detail="Sin Usuarios")
    return UserResponseSchema(**user_data)


async def get_users_by_filter(filters: BaseFilterShema) -> list[UserResponseSchema]:
    user_rows = await userRepository.get_user_by_filter(filters)
    return [UserResponseSchema(**row) for row in user_rows]


async def get_user_by_email(email: str) -> UserResponseSchema:
    user_data = await userRepository.get_user_by_email(email)
    if not user_data:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return UserResponseSchema(**user_data)


async def post_user_create(userCreate: UserCreateSchema) -> UserResponseSchema:
    user_data = await userRepository.post_user_create(userCreate)
    return UserResponseSchema(**user_data)


class UserService:
    get_user_all = staticmethod(get_user_all)
    get_user_by_email = staticmethod(get_user_by_email)
    get_users_by_filter = staticmethod(get_users_by_filter)
    post_user_create = staticmethod(post_user_create)


userService = UserService()
