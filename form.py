import sys
import json
import inspect

def tools():
    print("barri")

class Explore:
   age = 23
   name = "barri"

print("== "*10)
print(type(sys.deactivate_stack_trampoline))
print("== "*10)
print(type(sys.builtin_module_names))
print("== "*10)
print(sys.api_version, "== "*10)
print(sys.platform, "== "*10)




print(help(Explore),"== "*10, dir(tools))
print(type(tools))
print(inspect.isfunction(tools))
print(sys.platform,sys.version_info )
print("=> "*10)

print(dir(sys))
