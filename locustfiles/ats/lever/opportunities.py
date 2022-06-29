import json
import random

from locust import TaskSet, task, tag

from api.lever.instance_generator import random_opportunity


class OpportunityTask(TaskSet):
    @task(1)
    @tag("opportunity", "create")
    def create(self):
        params = {"perform_as": "4a253e29-4010-401b-8cef-d18aa9e55ad5"}

        payload = random_opportunity()

        res = self.client.post(
            "/opportunities",
            auth=self.user.get_auth(),
            params=params,
            data=json.dumps(payload),
            headers=self.user.headers,
            name="/opportunities",
        )

        print(res.status_code, payload["owner"])
