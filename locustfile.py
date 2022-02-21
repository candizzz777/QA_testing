from locust import HttpUser, task

class DudkaUser(HttpUser):
    @task
    def dudka_user(self):

        self.client.get("https://staging.kyivindependent.com/culture/6-last-minute-gift-ideas-from-ukrainian-brands/", auth=('kyivindependent', 'kyivindependent'))
