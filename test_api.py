import pytest
import requests

def test_jsonplaceholder_get():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    assert response.status_code == 200
    assert response.json()['id'] == 1

def test_jsonplaceholder_post():
    payload = {"title": "foo", "body": "bar"}
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=payload)
    assert response.status_code == 201
    assert response.json()['title'] == "foo"
