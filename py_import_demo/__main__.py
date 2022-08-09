import importlib
import pkgutil

from . import plugins

for plugin_info in pkgutil.iter_modules(plugins.__path__):
    importlib.import_module(f".{plugin_info.name}", package=plugins.__name__)

if __name__ == "__main__":
    print("Loaded plugin classes:\n" + "\n".join(str(c) for c in plugins.ALL))
