import json
from typing import Union


class JsonParser:
    def __init__(self, file: str) -> None:
        self.file = file
        self.loaded = self.__read__()

    def __read__(self) -> dict:
        with open(self.file, "r") as f:
            return json.load(f)
        
    def write(self, data: dict) -> None:
        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)

    def get(self, key: str) -> Union[str, int, float, bool, list, dict]:
        return self.loaded[key]
