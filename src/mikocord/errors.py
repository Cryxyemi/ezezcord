class NoSetupFound(Exception):
    """Raised when no setup function is found in the module."""

    def __init__(self, module: str):
        self.module = module
        super().__init__(f"No setup function found in {module}.")

    def __str__(self):
        return f"No setup function found in {self.module}."


class NoDatabaseFound(Exception):
    """Raised when no database is found in the config file"""

    def __init__(self, config: dict):
        self.config = config
        try:
            self.config["token"] = "REDACTED"
        except KeyError:
            pass

        super().__init__(f"No database found in {self.config}")

    def __str__(self):
        return f"No database found in {self.config}"
