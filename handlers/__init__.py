import os
import importlib

handlers = {}

dir_path = os.path.dirname(__file__)
for filename in os.listdir(dir_path):
    if filename.endswith(".py") and not filename.startswith("__"):
        module_name = filename[:-3]
        module = importlib.import_module(f"handlers.{module_name}")
        handlers[module_name] = module.handle
