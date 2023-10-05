#!//usr/bin/python3
import importlib.util
import dis

module_name = "hidden_4"
spec = importlib.util.spec_from_file_location(module_name, "hidden_4.pyc")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

names = []

for name in dir(module):
    if not name.startswith("__"):
        names.append(name)

names.sort()

for name in names:
    print(name)
