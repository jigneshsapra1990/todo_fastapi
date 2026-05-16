import pytest
from fastapi.testclient import TestClient
from app.app import app

client = TestClient(app)


# ── CREATE ────────────────────────────────────────────────────────────────────

def test_create_todo():
    r = client.post("/todo/", json={"title": "test1", "description": "desc", "isCompleted": False})
    assert r.status_code == 200
    assert r.json()["message"] == "Todo created successfully"
    assert r.json()["data"]["title"] == "test1"

def test_create_todo_without_description():
    r = client.post("/todo/", json={"title": "test2"})
    assert r.status_code == 200
    assert r.json()["data"]["description"] is None

def test_create_todo_title_too_short():
    r = client.post("/todo/", json={"title": "ab"})
    assert r.status_code == 422

def test_create_todo_title_too_long():
    r = client.post("/todo/", json={"title": "this is too long"})
    assert r.status_code == 422

def test_create_todo_missing_title():
    r = client.post("/todo/", json={"description": "no title"})
    assert r.status_code == 422


# ── GET ALL ───────────────────────────────────────────────────────────────────

def test_get_all_todos():
    r = client.get("/todo/")
    assert r.status_code == 200
    assert r.json()["message"] == "List of TODO items"
    assert isinstance(r.json()["data"], list)


# ── GET BY ID ─────────────────────────────────────────────────────────────────

def test_get_todo_by_id():
    created = client.post("/todo/", json={"title": "test3", "isCompleted": False})
    todo_id = created.json()["data"]["id"]
    r = client.get(f"/todo/{todo_id}")
    assert r.status_code == 200
    assert r.json()["data"]["id"] == todo_id

def test_get_todo_not_found():
    r = client.get("/todo/999999")
    assert r.status_code == 404
    assert r.json()["detail"] == "Todo not found"


# ── UPDATE ────────────────────────────────────────────────────────────────────

def test_update_todo():
    created = client.post("/todo/", json={"title": "test4", "isCompleted": False})
    todo_id = created.json()["data"]["id"]
    r = client.put(f"/todo/{todo_id}", json={"title": "updated", "isCompleted": True})
    assert r.status_code == 200
    assert r.json()["message"] == "Todo updated successfully"
    assert r.json()["data"]["title"] == "updated"

def test_update_todo_not_found():
    r = client.put("/todo/999999", json={"title": "updated", "isCompleted": True})
    assert r.status_code == 404
    assert r.json()["detail"] == "Todo not found"


# ── DELETE ────────────────────────────────────────────────────────────────────

def test_delete_todo():
    created = client.post("/todo/", json={"title": "test5", "isCompleted": False})
    todo_id = created.json()["data"]["id"]
    r = client.delete(f"/todo/{todo_id}")
    assert r.status_code == 200
    assert r.json()["message"] == "Todo deleted successfully"

def test_delete_todo_not_found():
    r = client.delete("/todo/999999")
    assert r.status_code == 404
    assert r.json()["detail"] == "Todo not found"

def test_delete_todo_then_get():
    created = client.post("/todo/", json={"title": "test6", "isCompleted": False})
    todo_id = created.json()["data"]["id"]
    client.delete(f"/todo/{todo_id}")
    r = client.get(f"/todo/{todo_id}")
    assert r.status_code == 404
