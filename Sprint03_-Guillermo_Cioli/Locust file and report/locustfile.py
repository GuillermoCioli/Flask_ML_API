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
    
    @task
    def predict(self):
        files = {"file": open("stress_test/dog.jpeg", "rb")}
        self.client.post("/predict", files=files)
    
    @task
    def feedback(self):
        feedback = {
            "filename": "random_file.jpg",
            "prediction": "cat",
            "score": 0.8
        }
        self.client.post("/feedback", data={"report": json.dumps(feedback)})
    
    @task
    def display(self):
        self.client.get("/display/0a7c757a80f2c5b13fa7a2a47a683593.jpeg")