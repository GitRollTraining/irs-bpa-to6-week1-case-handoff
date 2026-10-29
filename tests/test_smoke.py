"""Bootstrap checks only; these do not assess the five client features."""

from app import create_app
from fastapi.testclient import TestClient


def test_boots_and_serves_page_and_styles():
    with TestClient(create_app()) as client:
        page = client.get("/")
        assert page.status_code == 200
        assert "Your workspace starts here." in page.text
        assert client.get("/static/styles.css").status_code == 200
        assert client.get("/health").json() == {"status": "ok"}


def test_optional_title_reaches_api_configuration(monkeypatch):
    monkeypatch.setenv("APP_TITLE", "Training workspace")
    with TestClient(create_app()) as client:
        assert client.get("/openapi.json").json()["info"]["title"] == "Training workspace"


def test_project_files_are_not_public_routes():
    with TestClient(create_app()) as client:
        for path in ("/.env", "/pyproject.toml", "/data/evaluation.json", "/static/../.env"):
            assert client.get(path).status_code == 404
