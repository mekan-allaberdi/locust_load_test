from common.secret import personio_auth_params_list as auth_param_list
from employee import EmployeeTask
from absence import AbsenceTask

from locust import HttpUser, between


class PersonioUser(HttpUser):
    def __init__(self, parent):
        super(PersonioUser, self).__init__(parent)
        self.token = None
        self.auth_params = None
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

    auth_param_pointer = 0

    def on_start(self):
        self.auth_params = auth_param_list[PersonioUser.auth_param_pointer]
        PersonioUser.auth_param_pointer = (PersonioUser.auth_param_pointer + 1) % len(
            auth_param_list
        )
        self.authenticate()

    tasks = [EmployeeTask, AbsenceTask]
    wait_time = between(1, 2)
    host = "https://api.personio.de/v1"

    def authenticate(self):
        with self.client.post(
            url="/auth",
            headers=self.headers,
            params=self.auth_params,
            name="/auth",
            catch_response=True,
        ) as response:
            if response.status_code == 200:
                self.token = response.json()["data"]["token"]

    def get_auth_headers(self):
        return {**self.headers, "Authorization": "Bearer {}".format(self.token)}
