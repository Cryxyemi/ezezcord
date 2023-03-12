import json
from typing import Union


class JsonParser:
    """
    A simple JSON parser class.

    Private methods
    ---------------
        `__read__`` -> Reads the file and returns a dict.

    Public methods
    --------------
    ``write`` -> Writes data to the file.
        
    ``get`` -> Gets a value from the file.
     """
    def __init__(self, file: str) -> None:
        self.file = file
        self.loaded = self.__read__()

    def __read__(self) -> dict:
        with open(self.file, "r") as f:
            return json.load(f)
        
    def write(self, data: dict) -> None:
        with open(self.file, "w") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def get(self, key: str) -> Union[str, int, float, bool, list, dict]:
        try:
            return self.loaded[key]
        except KeyError:
            raise KeyError(f"Key {key} not found in {self.file}")
