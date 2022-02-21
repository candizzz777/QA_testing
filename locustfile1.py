import time
# from locust import HttpUser, task, between

class QuickstartUser:
    # wait_time = between(1, 5)
    def __init__(self, client):
        self.client = client

    # @task
    # def hello_world(self):
    #     self.client.get("/hello")
    #     self.client.get("/world")

    # @task(3)
    def view_items(self):
        for item_id in range(10):
            self.client.get(f"/item?id={item_id}", name="/item")
            time.sleep(1)
    #
    # def on_start(self):
    #     self.client.post("/login", json={"username":"foo", "password":"bar"})

a = QuickstartUser(1)

print(a.view_items())



