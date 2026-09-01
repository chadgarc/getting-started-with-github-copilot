from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant():
    activity_name = "Chess Club"
    email = "student@mergington.edu"

    # Ensure the participant is not already registered.
    current = client.get("/activities").json()
    if email in current[activity_name]["participants"]:
        client.delete(f"/activities/{activity_name}/participants/{email}")

    signup_response = client.post(f"/activities/{activity_name}/signup?email={email}")
    assert signup_response.status_code == 200

    delete_response = client.delete(f"/activities/{activity_name}/participants/{email}")
    assert delete_response.status_code == 200
    assert email not in client.get("/activities").json()[activity_name]["participants"]
