import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a yaml file and returns a ConfigBox object."""
    try:
        with open(path_to_yaml, 'r') as stream:
            content = ConfigBox(yaml.safe_load(stream))
            logger.info(f"Yaml file read successfully: {path_to_yaml}")
            return content
    except BoxValueError as e:
        logger.error(f"Error reading yaml file: {e}")
        raise e
    except Exception as e:
        logger.error(f"Error reading yaml file: {e}")
        raise e
    
@ensure_annotations
def create_directories(path_to_directories : list, verbose = True):
    """Creates directories if they don't exist."""
    for directory in path_to_directories:
        os.makedirs(directory, exist_ok=True)
        if verbose:
            logger.info(f"Directory created: {directory}")

@ensure_annotations
def get_size(path: Path) -> str:
    """Gets the size of a directory."""
    size_in_kb = round(os.path.getsize(path) / 1024, 2)
    return f"{size_in_kb} KB"