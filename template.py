## to setup project setup

import os
from pathlib import Path
import logging # to log the setup process

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s') # Set up logging

#specify project name 
project_name = "African-Name-NER"

list_of_files = [
    ".github/workflows/.gitkeep", # GitHub workflow file to keep the directory
    f"{project_name}/__init__.py", # Init file for the project package for local pacage imports
    f"{project_name}/data/__init__.py", # Init file for components package 
    f"{project_name}/data/raw/__init__.py", # Init file for components package   
    
    
]