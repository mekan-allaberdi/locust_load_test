import json
from locust import TaskSet, task, tag

from api.personio.instance_generator import random_attendance, random_attendance_list
from common.utils import get_next_token
from api.personio.data import random_attendance_id


class AttendanceTask(TaskSet):
    @task(1)
    @tag("attendances", "list", "unavailable")
    @get_next_token
    def list(self):
        return self.client.get(
            url="/company/attendances",
            headers=self.user.get_auth_headers(),
            name="/attendances",
        )

    @task(10)
    @tag("attendances", "create")
    @get_next_token
    def create(self):
        payload = {
            "attendances": random_attendance_list(),
        }
        return self.client.post(
            "/company/attendances/",
            data=json.dumps(payload),
            headers=self.user.get_auth_headers(),
            name="/attendances",
        )

    @task(5)
    @tag("attendances", "update")
    @get_next_token
    def update(self):
        payload = random_attendance()
        return self.client.patch(
            "/company/attendances/" + random_attendance_id(),
            data=json.dumps(payload),
            headers=self.user.get_auth_headers(),
            name="/attendances",
        )

    @task(1)
    @tag("attendances", "delete")
    @get_next_token
    def delete(self):
        return self.client.delete(
            "/company/attendances/" + random_attendance_id(),
            headers=self.user.get_auth_headers(),
            name="/attendances/",
        )
