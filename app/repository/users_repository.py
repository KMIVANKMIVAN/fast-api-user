from typing import List, Optional
from sqlmodel import select
from app.core.database import get_session
from app.model.users_model import UserModel
from app.schemas.users_shema import UserCreateSchema
from app.schemas.base_shema import BaseFilterShema


async def get_user_all() -> Optional[UserModel]:
    async for session in get_session():
        statement = select(UserModel)
        result = await session.exec(statement)
        return result.first()


async def get_users_by_filter(filters: BaseFilterShema) -> List[UserModel]:
    async for session in get_session():
        statement = select(UserModel)
        if filters.status is not None:
            statement = statement.where(UserModel.status == filters.status)
        if filters.userCreate is not None:
            statement = statement.where(UserModel.userCreate == filters.userCreate)
        if filters.userUpdate is not None:
            statement = statement.where(UserModel.userUpdate == filters.userUpdate)
        if filters.dateCreate is not None:
            statement = statement.where(UserModel.dateCreate == filters.dateCreate)
        if filters.dateUpdate is not None:
            statement = statement.where(UserModel.dateUpdate == filters.dateUpdate)

        limit = filters.limit or 10
        offset = ((filters.page or 1) - 1) * limit
        statement = statement.offset(offset).limit(limit)

        result = await session.exec(statement)
        return result.all()


async def get_user_by_email(email: str) -> Optional[UserModel]:
    async for session in get_session():
        statement = select(UserModel).where(UserModel.email == email)
        result = await session.exec(statement)
        return result.first()


async def post_user_create(user: UserCreateSchema) -> UserModel:
    async for session in get_session():
        db_user = UserModel.model_validate(user)
        session.add(db_user)
        await session.commit()
        await session.refresh(db_user)
        return db_user


class UserRepository:
    get_user_all = staticmethod(get_user_all)
    get_user_by_email = staticmethod(get_user_by_email)
    get_user_by_filter = staticmethod(get_users_by_filter)
    post_user_create = staticmethod(post_user_create)


userRepository = UserRepository()
