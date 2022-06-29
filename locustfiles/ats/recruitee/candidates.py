import json
import random

from locust import TaskSet, task, tag
from api.recruitee.data import random_candidate_id, random_offer_id, random_offers
from api.recruitee.instance_generator import random_candidate

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
            "offers": random_offers(),
        }

        self.client.post(
            "/candidates",
            data=json.dumps(payload),
            headers=self.user.get_auth_headers(),
            name="/candidates",
        )

    @task(1)
    @tag("candidates", "detail")
    def detail(self):
        candidate_id = random_candidate_id()

        return self.client.get(
            "/candidates/{}".format(candidate_id),
            headers=self.user.get_auth_headers(),
            name="/candidates/candidate_id",
        )

    @task(1)
    @tag("candidates", "offers")
    def offer_detail(self, offer_id=None):
        offer_id = offer_id or random_offer_id()

        return self.client.get(
            "/offers/{}".format(offer_id),
            headers=self.user.get_auth_headers(),
            name="/offers/offer_id",
        )

    @task(1)
    @tag("candidates", "placements", "change_stage")
    def change_stage(self):
        try:
            # Step-1: Get placement info from candidate profile
            candidate_info = self.detail().json()

            placement = random.choice(candidate_info["candidate"]["placements"])

            # Step-2: Get new stage from offer detail
            offer_info = self.offer_detail(placement["offer_id"]).json()

            stage = random.choice(offer_info["offer"]["pipeline_template"]["stages"])

            params = {
                "stage_id": stage["id"],
            }

            self.client.patch(
                "/placements/{}/change_stage".format(placement["id"]),
                params=params,
                headers=self.user.get_auth_headers(),
                name="placements/change_stage",
            )
        except Exception as e:
            print("Oops!", e.__class__, "occurred.")
            print("Next entry.")
            print()

    @task(1)
    @tag("candidates", "placements", "only")
    def create(self):
        params = {
            "candidate_id": random_candidate_id(),
            "offer_id": random_offer_id(),
        }

        res = self.client.post(
            "/placements",
            params=params,
            headers=self.user.get_auth_headers(),
            name="/placements",
        )
