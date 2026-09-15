class Application:
    """" Represent an Application with a status"""


    def __init__(self, job:str, status="pending"):
        self.job = job
        self.status = status

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if not status in ["pending", "accepted", "rejected"]:
            raise ValueError("Invalid Status")
        self._status = status

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, job):
        if not job in ["cook", "waiter", "cashier"]:
            raise ValueError("Invalid Job")
        self._job = job