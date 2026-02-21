import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from backend.controllers import auth_controller
from backend.models.User import User


class TestAuthController:
    @pytest.mark.asyncio
    async def test_get_user_by_username_exists(self, db: AsyncSession, test_user: User):
        user = await auth_controller.get_user_by_usename(db, "pasanca_7")

        assert user is not None
        assert user.username == "pasanca_7"
        assert user.email == "pasanca_7@example.com"

    @pytest.mark.asyncio
    async def test_get_user_by_username_not_exists(self, db: AsyncSession):
        user = await auth_controller.get_user_by_usename(db, "no_user")

        assert user is None
