import pytest

from backend.controllers import players_controller


class TestPlayerController:

    @pytest.mark.asyncio
    async def test_get_player(self, db_with_player):
        player = await players_controller.get_player_by_id(db_with_player, 15956)
        assert player is not None
        assert player.name == "Jesús Navas"

    @pytest.mark.asyncio
    async def test_get_player_None(self, db_with_player):
        player = await players_controller.get_player_by_id(db_with_player, 0)
        assert player is None
