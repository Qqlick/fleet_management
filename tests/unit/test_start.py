def test_init():
    # this is just dummy test to check if CICD pipeline working
    assert True


def test_client(client):
    resp = client.get("/")
    assert resp.status_code == 200
