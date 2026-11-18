import pytest
from fastapi.testclient import TestClient
from src.app import app, clear_tasks

# Une fixture de test (ou banc/cadre de test) est un ensemble d'éléments
# (code, données ou dispositif physique) conçu pour placer un système 
# dans un état connu et fixe afin d'exécuter des tests de manière reproductible.
# Rôle : Préparer l'environnement (jeu de données, base de données de test,
# objets simulés ou mocks) avant de lancer un test, puis nettoyer après son 
# exécution.
# Objectif : Éviter la duplication de code et garantir que les tests 
# donnent toujours les mêmes résultats, indépendamment de l'état du système.
@pytest.fixture(autouse=True)
def clean_tasks():
    """
    Clear all tasks before each test.
    This ensures tests don't interfere with each other.
    """
    clear_tasks()
    yield
    clear_tasks()


@pytest.fixture
def client():
    """
    Provide a test client for making API requests.

    Usage in tests:
        def test_something(client):
            response = client.get("/tasks")
            assert response.status_code == 200
    """
    with TestClient(app) as test_client:
        yield test_client
