"""
docker-gui: an easy to use docker gui for gtk3.
"""
from .data.config import __version__
from . import gui
from . import src


__all__ = [
    "src",
    "gui",
    "__version__",
]
