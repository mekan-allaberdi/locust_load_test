from locust import TaskSet, task, tag

from api.personio.instance_generator import random_time_off, random_time_off_type_id
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

    @task(1)
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

    @task(1)
    @tag("absences", "delete", "unavailable")
    @get_next_token
    def delete(self):
        time_off_type_id = random_time_off_type_id()
        return self.client.delete(
            "/company/time-offs/{}".format(time_off_type_id),
            headers=self.user.get_auth_headers(),
            name="/company/time-offs/",
        )

    @task(5)
    @tag("absences", "detail", "unavailable")
    @get_next_token
    def detail(self):
        return self.client.get(
            "/company/time-offs/" + "11",  # fix after documentation is updated
            headers=self.user.get_auth_headers(),
            name="/company/time-offs/",
        )
