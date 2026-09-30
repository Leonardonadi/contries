from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_countries():
    response = client.get("/countries")
    assert response.status_code == 200
    assert sorted(response.json()) == ["England", "France", "Germany", "Italy", "Peru", "Portugal", "Spain"]


def test_cities():
    """Only return cities included in the API data for Spain."""
    response = client.get("/countries/Spain")
    assert response.status_code == 200
    cities = response.json()
    assert cities == ["Seville"]
    assert "Madrid" not in cities