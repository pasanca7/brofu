class TestPlayerRouters:

    def test_get_player_routers(self, mocker, client, player_1):
        # Mocks
        mocker_get_player = mocker.patch(
            "backend.controllers.players_controller.get_player_by_id"
        )
        mocker_get_player.return_value = player_1

        # endpoint to test
        response = client.get("/players/15956")

        # Assertions
        assert response.status_code == 200
        assert response.json()["id"] == player_1.id
        assert response.json()["name"] == player_1.name

    def test_get_player_routers_not_found(self, mocker, client):
        # Mocks
        mocker_get_player = mocker.patch(
            "backend.controllers.players_controller.get_player_by_id"
        )
        mocker_get_player.return_value = None

        # Endpoint to test
        response = client.get("/players/0")

        # Assertions
        assert response.status_code == 404

    def test_search_player_router(self, mocker, client, players):
        # Mocks
        mocker_search_player = mocker.patch(
            "backend.controllers.players_controller.search_players_by_name"
        )
        mocker_search_player.return_value = players

        # Endpoint to test
        response = client.get("/players/search?name=Jesus")

        # Assertions
        assert response.status_code == 200
        assert len(response.json()) == 2
        assert response.json()[0]["first_name"] == "Jesús"
        assert response.json()[1]["first_name"] == "Keylor"

    def test_search_player_router_empty(self, mocker, client):
        # Mocks
        mocker_search_player = mocker.patch(
            "backend.controllers.players_controller.search_players_by_name"
        )
        mocker_search_player.return_value = []

        # Endpoint to test
        response = client.get("/players/search?name=XXX")

        # Assertions
        assert response.status_code == 200
        assert len(response.json()) == 0
