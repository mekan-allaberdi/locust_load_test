from common.constants import WORKABLE

from locust import HttpUser, between
from locustfiles.ats.lever.opportunities import OpportunityTask


class LeverUser(HttpUser):
    def __init__(self, parent):
        super(LeverUser, self).__init__(parent)
        self.username = ""
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

    tasks = [OpportunityTask]
    wait_time = between(0.5, 1)
    host = "https://api.lever.co/v1"

    def get_auth(self):
        return (self.username, "")