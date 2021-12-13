import json
from locust import TaskSet, task, tag

from common.data_gen import random_employee
from common.api_test_data import random_employee_id
from common.utils import get_next_token


class EmployeeTask(TaskSet):
    @task(1)
    @tag("employees", "list")
    @get_next_token
    def list(self):
        return self.client.get(
            url="/company/employees",
            headers=self.user.get_auth_headers(),
            name="/employees",
        )

    @task
    @tag("employees", "create", "unavailable")
    @get_next_token
    def create(self):
        payload = {
            "employee": random_employee(),
        }
        return self.client.post(
            "/company/employees/",
            data=json.dumps(payload),
            headers=self.user.get_auth_headers(),
            name="/employees",
        )

    @task(5)
    @tag("employees", "update")
    @get_next_token
    def update(self):
        employee_id = random_employee_id()
        payload = {"employee": random_employee()}
        return self.client.patch(
            "/company/employees/{}".format(employee_id),
            data=json.dumps(payload),
            headers=self.user.get_auth_headers(),
            name="/employees",
        )

    @task(10)
    @tag("employees", "detail")
    @get_next_token
    def detail(self):
        employee_id = random_employee_id()
        return self.client.get(
            "/company/employees/{}".format(employee_id),
            headers=self.user.get_auth_headers(),
            name="/employees/employee_id",
        )

    @task(10)
    @tag("employees", "absences_balance")
    @get_next_token
    def absences_balance(self):
        employee_id = random_employee_id()
        return self.client.get(
            "/company/employees/{}/absences/balance".format(employee_id),
            headers=self.user.get_auth_headers(),
            name="/employees/absences/balance",
        )

    @task(5)
    @tag("employees", "custom-attributes")
    @get_next_token
    def custom_attributes(self):
        return self.client.get(
            "/company/employees/custom-attributes",
            headers=self.user.get_auth_headers(),
            name="/employees/custom-attributes",
        )
