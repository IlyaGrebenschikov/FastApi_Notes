import pytest
from httpx import AsyncClient
from fastapi import status

from app.main import app


@pytest.mark.asyncio
async def test_startup() -> None:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get(
            '/'
        )

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'hello': 'world'}
