from common.constants import WORKABLE

from locust import HttpUser, between
from locustfiles.ats.workable.candidates import CandidateTask


class WorkableUser(HttpUser):
    def __init__(self, parent):
        super(WorkableUser, self).__init__(parent)
        self.tool = WORKABLE
        self.token = ""
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

    tasks = [CandidateTask]
    wait_time = between(0.3, 0.5)
    host = "https://vacuumlabs.workable.com/spi/v3/"

    def get_auth_headers(self):
        return {**self.headers, "Authorization": "Bearer {}".format(self.token)}
