from common.constants import WORKABLE

from locust import HttpUser, between
from locustfiles.ats.recruitee.candidates import CandidateTask


class RecruiteeUser(HttpUser):
    def __init__(self, parent):
        super(RecruiteeUser, self).__init__(parent)
        self.token = "SAMPLE_TOKEN"
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

    tasks = [CandidateTask]
    wait_time = between(2, 3)
    host = "https://api.recruitee.com/c/{}".format("SAMPLE_ID")

    def get_auth_headers(self):
        return {**self.headers, "Authorization": "Bearer {}".format(self.token)}
