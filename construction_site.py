class ConstructionSite:
    def __init__(self, start_date) -> None:
        self._start_date = start_date

    def progressAt(self) -> str:
        return self._start_date