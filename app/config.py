import sys
import os

from pathlib import Path


def get_project_root() -> Path:
    return Path(__file__).parent.parent


def create_project_root() -> None:
    root = os.path.join(os.path.dirname(get_project_root()), 'Fast_Api_Notes')
    sys.path.append(root)
