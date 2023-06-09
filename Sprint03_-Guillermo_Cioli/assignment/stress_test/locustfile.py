from locust import HttpUser, between, task
import json

class APIUser(HttpUser):
    # Put your stress tests here.
    # See https://docs.locust.io/en/stable/writing-a-locustfile.html for help.
    # TODO
    wait_time = between(1, 5)
    
    @task
    def index(self):
        self.client.get("/")
        assert resp.status_code == 200, f"Expected status code 200, but got {resp.status_code}"

    @task
    def predict(self):
        with open("dog.jpeg", "rb") as f:

            files = {"file": f}
            resp = self.client.post("/predict", files=files)
            assert json.loads(resp.text)["success"] is True
        
    @task
    def feedback(self):
        # Submit some fake feedback
        feedback = {
            "filename": "random_file.jpg",
            "prediction": "cat",
            "score": 0.8
        }
        resp = self.client.post("/feedback", data={"report": json.dumps(feedback)})
        assert resp.ok, "Failed to submit feedback with status code: {}".format(resp.status_code)
    
    @task
    def display(self):
        resp = self.client.get("/display/0a7c757a80f2c5b13fa7a2a47a683593.jpeg")
        assert resp.status_code == 200, f"Expected status code 200, but got {resp.status_code}"