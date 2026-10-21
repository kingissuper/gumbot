# AI generated (changed the __all__.append myself)
import importlib
import pkgutil
__all__ = []
for _, module_name, _ in pkgutil.iter_modules(__path__):
    __all__.append(importlib.import_module(f"{__name__}.{module_name}"))
    #__all__.append(module_name)