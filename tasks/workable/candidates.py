import json
import random
from datetime import datetime

from locust import TaskSet, task, tag

from api.workable.instance_generator import (
    random_candidate,
    random_comment,
    random_disqualification_reason,
    random_tags,
)
from api.workable.data import (
    random_candidate_id,
    random_job_shortcode,
    random_member_id,
    random_stage,
)
from common.utils import random_date


def list_candidates(tag_name):
    def wrap(func):
        def wrapped_func(*args, **kwargs):
            user = args[0].user
            query_params = func(*args, **kwargs)
            query_params["limit"] = "100"
            user.client.get(
                "/candidates",
                headers=user.get_auth_headers(),
                params=query_params,
                name="/candidates:{}".format(tag_name),
            )

        return wrapped_func

    return wrap


class CandidateTask(TaskSet):
    url = "https://vacuumlabs.workable.com/spi/v3/candidates?limit=100&since_id=97954ac"
    total = 0

    @task(1)
    @tag("candidates", "list")
    @list_candidates("default")
    def list(self):
        return {}

    @task(1)
    @tag("candidates", "list", "with_job_shortcode")
    @list_candidates("with_job_shortcode")
    def list_by_shortcode(self):
        return {"shortcode": random_job_shortcode()}

    @task(1)
    @tag("candidates", "list", "filtered")
    @list_candidates("filtered")
    def list_filltered(self):
        return {"updated_after": random_date().strstrftime()}

    @task(1)
    @tag("candidates", "create")
    def create(self):
        payload = {
            "candidate": random_candidate(),
            "sourced": random.choice([False, True, False]),
        }

        query_params = {} if payload["sourced"] else {"stage": random_stage()}

        shortcode = random_job_shortcode()
        self.client.post(
            "/jobs/{}/candidates".format(shortcode),
            params=query_params,
            data=json.dumps(payload),
            headers=self.user.get_auth_headers(),
            name="/candidates",
        )

    @task(1)
    @tag("candidates", "update")
    def update(self):
        candidate_id = random_candidate_id()
        payload = {
            "candidate": random_candidate(),
        }
        self.client.patch(
            "/candidates/{}".format(candidate_id),
            data=json.dumps(payload),
            headers=self.user.get_auth_headers(),
            name="/candidates",
        )

    @task(1)
    @tag("candidates", "detail")
    def detail(self):
        candidate_id = random_candidate_id()
        self.client.get(
            "/candidates/{}".format(candidate_id),
            headers=self.user.get_auth_headers(),
            name="/candidates/:id",
        )

    @task(1)
    @tag("candidates", "activities")
    def activities(self):
        candidate_id = random_candidate_id()
        self.client.get(
            "/candidates/{}/activities".format(candidate_id),
            headers=self.user.get_auth_headers(),
            name="/candidates/:id/activities",
        )

    @task(1)
    @tag("candidates", "offer")
    def activities(self):
        candidate_id = random_candidate_id()
        self.client.get(
            "/candidates/{}/offer".format(candidate_id),
            headers=self.user.get_auth_headers(),
            name="/candidates/:id/offer",
        )

    @task(1)
    @tag("candidates", "comments")
    def comments(self):
        candidate_id = random_candidate_id()
        payload = {
            "member_id": random_member_id(),
            "comment": random_comment(),
        }

        self.client.post(
            "/candidates/{}/comments".format(candidate_id),
            data=json.dumps(payload),
            headers=self.user.get_auth_headers(),
            name="/candidates/:id/comments",
        )

    @task(1)
    @tag("candidates", "tags")
    def tags(self):
        candidate_id = random_candidate_id()
        payload = {
            "tags": random_tags(),
        }

        self.client.put(
            "/candidates/{}/tags".format(candidate_id),
            data=json.dumps(payload),
            headers=self.user.get_auth_headers(),
            name="/candidates/:id/tags",
        )

    @task(1)
    @tag("candidates", "disqualify")
    def disqualify(self):
        candidate_id = random_candidate_id()
        payload = {
            "member_id": random_member_id(),
            "disqualification_reason": random_disqualification_reason(),
        }

        self.client.post(
            "/candidates/{}/disqualify".format(candidate_id),
            data=json.dumps(payload),
            headers=self.user.get_auth_headers(),
            name="/candidates/:id/disqualify",
        )

    @task(1)
    @tag("candidates", "revert")
    def revert(self):
        candidate_id = random_candidate_id()
        payload = {
            "member_id": random_member_id(),
        }

        self.client.post(
            "/candidates/{}/revert".format(candidate_id),
            data=json.dumps(payload),
            headers=self.user.get_auth_headers(),
            name="/candidates/:id/revert",
        )

    @task(1)
    @tag("candidates", "copy_or_relocate")
    def copy_or_relocate(self):
        candidate_id = random_candidate_id()
        payload = {
            "member_id": random_member_id(),
            "target_job_shortcode": random_job_shortcode(),
            "target_stage": random_stage(),
        }
        action = random.choice(["copy", "relocate"])

        self.client.post(
            "/candidates/{}/{}".format(candidate_id, action),
            data=json.dumps(payload),
            headers=self.user.get_auth_headers(),
            name="/candidates/:id/{}".format(action),
        )

    @task(1)
    @tag("candidates", "move")
    def move(self):
        candidate_id = random_candidate_id()
        payload = {
            "member_id": random_member_id(),
            "target_stage": random_stage(),
        }

        self.client.post(
            "/candidates/{}/move".format(candidate_id),
            data=json.dumps(payload),
            headers=self.user.get_auth_headers(),
            name="/candidates/:id/move",
        )

    @task(1)
    @tag("candidates", "ratings")
    def ratings(self):
        candidate_id = random_candidate_id()
        payload = {
            "member_id": random_member_id(),
            "comment": random_comment(),
            "score": random.choice(["positive", "negative", "definitely"]),
        }

        self.client.post(
            "/candidates/{}/ratings".format(candidate_id),
            data=json.dumps(payload),
            headers=self.user.get_auth_headers(),
            name="/candidates/:id/ratings",
        )
