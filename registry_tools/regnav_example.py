# -*- coding: UTF-8 -*-

#imports
import windows
from windows.generated_def import KEY_WRITE, KEY_READ, REG_QWORD

#got a registry object
registry = windows.system.registry

#navigate object to network interface manage key collections
network_registry = registry(r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet" \
                            r"\Control\Class\{4D36E972-E325-11CE-BFC1-08002BE10318}")

for key in network_registry.subkeys:

    print key