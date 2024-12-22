import importlib
import os


for package in filter(lambda x: os.path.isdir(x), os.listdir()):
    if "setup.py" in os.listdir(package):
        importlib.import_module(f"{package}.setup").setup()
        