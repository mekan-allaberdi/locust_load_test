import json
import random

from locust import TaskSet, task, tag
from api.recruitee.instance_generator import random_candidate
from common.utils import random_offer_list

from locustfiles.ats.common_tasks import list_candidates


class CandidateTask(TaskSet):
    @task(1)
    @tag("candidates", "list")
    @list_candidates("list")
    def list(self):
        return {}

    @task(1)
    @tag("candidates", "create")
    def create(self):
        payload = {
            "candidate": random_candidate(),
            "offers": random_offer_list(),
        }

        self.client.post(
            "/candidates",
            data=json.dumps(payload),
            headers=self.user.get_auth_headers(),
            name="/candidates",
        )