import os
import tempfile
import pytest
from main import create_app

@pytest.fixture
def client():
    app = create_app()

    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200