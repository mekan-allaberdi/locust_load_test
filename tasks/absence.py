import json
from locust import TaskSet, task, tag

from common.data_gen import random_attendance, random_time_off, random_time_off_type_id
from common.api_test_data import random_attendance_id
from common.utils import get_next_token, random_start_end_date


class AbsenceTask(TaskSet):
    @task(1)
    @tag("absences", "list" "time-off-types")
    @get_next_token
    def list(self):
        return self.client.get(
            url="/company/time-off-types",
            headers=self.user.get_auth_headers(),
            name="/company/time-off-types",
        )

    @task(1)
    @tag("absences", "list", "time-offs")
    @get_next_token
    def list(self):
        start_date, end_date = random_start_end_date()
        return self.client.get(
            url="/company/time-offs",
            params={"start_date": start_date, "end_date": end_date},
            headers=self.user.get_auth_headers(),
            name="/company/time-offs",
        )

    @task(10)
    @tag("absences", "create")
    @get_next_token
    def create(self):
        payload = random_time_off()
        return self.client.post(
            "/company/time-offs",
            json=payload,
            headers=self.user.get_auth_headers(),
            name="/company/time-offs",
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
            name="/absences",
        )

    @task(1)
    @tag("absences", "delete")
    @get_next_token
    def delete(self):
        return self.client.delete(
            "/company/time-offs/" + random_time_off_type_id(),
            headers=self.user.get_auth_headers(),
            name="/company/time-offs/",
        )

    @task(10)
    @tag("absences", "detail", "unavailable")
    @get_next_token
    def detail(self):
        return self.client.get(
            "/company/time-offs/" + "11",
            headers=self.user.get_auth_headers(),
            name="/company/time-offs/",
        )
