import pytest
from httpx import AsyncClient
from fastapi import status

from app.main import app

import asyncio


@pytest.fixture(scope="session")
def event_loop():
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.mark.asyncio(scope="session")
async def test_create_user() -> None:
    async with AsyncClient(app=app, base_url="http://0.0.0.0:8080") as ac:
        response = await ac.post(
            '/users/',
            json={
                'name': 'Ilya',
            },
        )

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        'name': 'Ilya',
        'id': 32
    }


@pytest.mark.asyncio(scope="session")
async def test_get_user() -> None:
    async with AsyncClient(app=app, base_url="http://0.0.0.0:8080") as ac:
        response = await ac.get(
            '/users/{id}?user_id=1',
        )

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "name": "aaaaa",
        "id": 1,
    }


@pytest.mark.asyncio(scope="session")
async def test_update_user() -> None:
    async with AsyncClient(app=app, base_url="http://0.0.0.0:8080") as ac:
        response = await ac.put(
            '/users/{id}?user_id=2',
            json={
                'name': 'Ilya'
            }
        )

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "name": "Ilya",
        "id": 2,
    }


@pytest.mark.asyncio(scope="session")
async def test_delete_user() -> None:
    async with AsyncClient(app=app, base_url="http://0.0.0.0:8080") as ac:
        response = await ac.delete(
            'http://0.0.0.0:8080/users/{id}?user_id=4'
        )

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'message': 'deleted'}
