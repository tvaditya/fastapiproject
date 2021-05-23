import json


def test_create_user(client):
    data = {
        "username":"testuser",
        "email":"testuser@nofoobar.com",
        "password":"testing"
    }

    response = client.post("/user/",json.dumps(data))
    print("test with sqllite")
    assert response.status_code == 200
    assert response.json()["email"] == "testuser@nofoobar.com"
    assert response.json()["is_active"] == True
