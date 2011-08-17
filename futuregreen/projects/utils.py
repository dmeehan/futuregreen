# projects/utils.py

def get_model(module_name):
    """Imports the model module_name."""
    mod = __import__(module_name)
    return mod