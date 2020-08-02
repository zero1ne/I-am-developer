from datetime import datetime


class Call():
    def __init__(self, start: datetime, end: datetime):
        self.start = start
        self.end = end

    def get_start(self) -> datetime:
        return self.start

    def get_end(self) -> datetime:
        return self.end