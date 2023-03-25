class NoSetupFound(Exception):
    """Raised when no setup function is found in the module."""

    def __init__(self, module: str):
        self.module = module
        super().__init__(f"No setup function found in {module}.")

    def __str__(self):
        return f"No setup function found in {self.module}."
