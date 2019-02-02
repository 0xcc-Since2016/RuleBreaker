# -*- coding: UTF-8 -*-

#imports
import windows 
import os.path 
import sys 
import pprint 

registry = windows.system.registry

SVC_Registry_lst = registry("HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services")

def get_Svc_Reg_Attribute(key, attr_name):

    try:
        return key[attr_name]
    except:
        print "[*]Error: Service %s has no attribute %s." % (key.name, attr_name)
        return None

for key in SVC_Registry_lst.subkeys:

    pprint.pprint(key)
    if len(key.values) > 0:
        print get_Svc_Reg_Attribute(key, "ImagePath")
        print get_Svc_Reg_Attribute(key, "Description")
        #print get_Svc_Reg_Attribute(key, "ImagePath")
        #print get_Svc_Reg_Attribute(key, "ImagePath")
        



# pprint.pprint(registry)
# #registry is a winobject - registry.
# print("Registry is <{0}>".format(registry))
# current_user = registry("HKEY_CURRENT_USER")
# print("HKEY_CURRENT_USER is <{0}>".format(current_user))
# subkeys_name = [s.name for s in current_user.subkeys]
# print("HKEY_CURRENT_USER subkeys names are:")
# pprint.pprint(subkeys_name)
# print("Opening 'Software' in HKEY_CURRENT_USER: {0}".format(current_user("Software")))
# print("We can also open it in one access: {0}".format(registry(r"HKEY_CURRENT_USER\Sofware")))
# print("Looking at CurrentVersion")
# windows_info = registry("HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion")
# print("Key is {0}".format(windows_info))
# print("values are:")
# pprint.pprint(windows_info.values)
# registered_owner = windows_info["RegisteredOwner"]
# print("registered owner = <{0}>".format(registered_owner))




