from rich.console import Console
from rich.prompt import Prompt

SUCCESS_STYLE = "green bold"
ERROR_STYLE = "red bold underline"
WARNING_STYLE = "orange3 bold underline"


# By Default the module is in quiet mode (no-prints)
out = Console(quiet=True)
err = Console(stderr=True, style=ERROR_STYLE)

# Exports
__all__ = [
    "Prompt",
    "out",
    "SUCCESS_STYLE",
    "ERROR_STYLE",
    "WARNING_STYLE",
]
