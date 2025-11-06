from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    # Simulate a user waiting between 1 and 5 seconds after each task
    wait_time = between(1, 5)

    @task
    def index_page(self):
        # This will make a GET request to the root URL of the host
        self.client.get("/")
