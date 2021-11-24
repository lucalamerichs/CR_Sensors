from datetime import datetime

class ConstructionSite:
    def __init__(self, start_date) -> None:
        self._start_date = datetime.strptime(start_date, "%Y-%m-%d")

    def progressAt(self) -> datetime:
        return self._start_date