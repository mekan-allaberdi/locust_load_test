from common.constants import WORKABLE

from locust import HttpUser, between
from tasks.workable.candidates import CandidateTask


class WorkableUser(HttpUser):
    def __init__(self, parent):
        super(WorkableUser, self).__init__(parent)
        self.tool = WORKABLE
        self.token = "9389c14ce0761c7691f21b8959e413a1f65578688dad2f1ef1eeca20b057b540"
        self.auth_params = None
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(self.token),
        }

    tasks = [CandidateTask]
    wait_time = between(0.3, 0.5)
    host = "https://vacuumlabs.workable.com/spi/v3/"

    def get_auth_headers(self):
        return {**self.headers, "Authorization": "Bearer {}".format(self.token)}
