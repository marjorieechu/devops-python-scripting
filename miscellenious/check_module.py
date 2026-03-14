import importlib

modules = ["venv", "pip", "requests"]

for module in modules:
    try:
        importlib.import_module(module)
        print(f"{module} is installed")
    except ImportError:
        print(f"{module} is NOT installed")

#python check_module.py