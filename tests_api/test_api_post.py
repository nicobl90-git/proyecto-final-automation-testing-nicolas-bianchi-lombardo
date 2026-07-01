import requests
from utils.loggers import logger
import pytest

CREATE_URL = 'https://reqres.in/api/users'
API_KEY = 'pro_687a35cc99c02c28f522221f8db090b1f52aceb1bd7134330b4649d5fa579c38'

@pytest.mark.api
def test_create_user():
    headers = {'x-api-key': API_KEY}
    payload = {'name': 'Matias QA', 'job': 'tester'}
    r = requests.post(CREATE_URL, json=payload, headers=headers)
    # print(f"\nStatus code: {r.status_code}")
    assert r.status_code == 201

    new_user = r.json()
    # print(f"Respuesta completa: {new_user}")
    assert new_user['name'] == 'Matias QA'
    # print(f"Nombre confirmado: {new_user['name']}")
    assert 'id' in new_user and 'createdAt' in new_user
    # print(f"ID asignado: {new_user['id']}")
    # print(f"Creado en: {new_user['createdAt']}")