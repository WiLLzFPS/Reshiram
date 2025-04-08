integrations = {}

# Decorator to register an integration
def register_integration(name):
    def decorator(func):
        integrations[name] = func
        return func
    return decorator

# Retrieve an integration by name
def get_integration(name):
    if name in integrations:
        return integrations[name]
    raise ValueError(f"Integration '{name}' not found.")