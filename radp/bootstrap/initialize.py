from .database import reset_database
from .runtime import get_runtime


def initialize_runtime(reset: bool):
    runtime = get_runtime()
    if reset:
        reset_database(runtime.settings.database)
    runtime.initialize()
