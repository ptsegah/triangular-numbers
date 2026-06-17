import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_index():
    r = client.get("/")
    assert r.status_code == 200


def test_triangular_true():
    for n in [0, 1, 3, 6, 10, 21, 55]:
        r = client.get(f"/triangular-numbers?num={n}")
        assert r.status_code == 200
        assert r.json()["is_triagular"] is True, f"{n} should be triangular"


def test_triangular_false():
    for n in [2, 4, 5, 7, 11, 28]:
        r = client.get(f"/triangular-numbers?num={n}")
        assert r.status_code == 200
        assert r.json()["is_triagular"] is False, f"{n} should not be triangular"


def test_negative():
    r = client.get("/triangular-numbers?num=-1")
    assert r.status_code == 200
