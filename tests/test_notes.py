import pytest
from httpx import AsyncClient
from fastapi import status

from app import app

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
async def test_create_note() -> None:
    async with AsyncClient(app=app, base_url="http://0.0.0.0:8080") as ac:
        response = await ac.post(
            '/notes/?user_id=2',
            json={
                "title": "Ilya",
                "subtitle": "Grebenschikov",
                "introduction": "is a real",
                "main_text": "mujik!!!!"
            }
        )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "title": "Ilya",
        "subtitle": "Grebenschikov",
        "introduction": "is a real",
        "main_text": "mujik!!!!",
        "user_id": 2,
        "id": 28
    }


@pytest.mark.asyncio(scope="session")
async def test_get_notes_many() -> None:
    async with AsyncClient(app=app, base_url="http://0.0.0.0:8080") as ac:
        response = await ac.get(
            '/notes/many{id}?user_id=36&limit=20',
        )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [
        {
            "title": "string",
            "subtitle": "string",
            "main_text": "string",
            "introduction": "string",
            "id": 15,
            "user_id": 36
        },
        {
            "title": "aaa",
            "subtitle": "bb",
            "main_text": "dd",
            "introduction": "cc",
            "id": 16,
            "user_id": 36
        }
    ]


@pytest.mark.asyncio(scope="session")
async def test_get_notes_one() -> None:
    async with AsyncClient(app=app, base_url="http://0.0.0.0:8080") as ac:
        response = await ac.get(
            '/notes/one{id}?user_id=36&note_id=16',
        )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "title": "aaa",
        "subtitle": "bb",
        "main_text": "dd",
        "id": 16,
        "introduction": "cc",
        "user_id": 36
    }


@pytest.mark.asyncio(scope="session")
async def test_update_note() -> None:
    async with AsyncClient(app=app, base_url="http://0.0.0.0:8080") as ac:
        response = await ac.put(
            '/notes/{id}?user_id=35&note_id=19',
            json={
                "title": "aa",
                "subtitle": "bb",
                "introduction": "cc",
                "main_text": "xx"
            }
        )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "title": "aa",
        "subtitle": "bb",
        "main_text": "xx",
        "id": 19,
        "introduction": "cc",
        "user_id": 35
    }


@pytest.mark.asyncio(scope="session")
async def test_delete_note() -> None:
    async with AsyncClient(app=app, base_url="http://0.0.0.0:8080") as ac:
        response = await ac.delete(
            '/notes/{id}?user_id=35&note_id=25'
        )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "result": "deleted"
    }
