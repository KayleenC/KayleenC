# The given script helps to easily grab the information from devices.
# It aims to manage all the devices well in our team.
# Usage: Tap the file name "device_info_<version>.py" on your terminal.
# PoC: MyLDAP@

---------------------------------------------------------------------------

import os
import time

def getSnList(command):
    action = os.popen(command)
    device_list = action.read()
    action.close()
    sn_list = device_list.split("\n")
    return sn_list

def _List(command):
    list_ = getSnList(command)
    sn = []
    for item in list_:
        if (item.stript() == ""):
            continue
        elif (item.startswitch("List of")):
            continue
        else:
            sn.append(item.split("\t")[0])
    return sn


### adb root
def adb_root(list):
    root = "adb -s " + list + " root"
    os.system(root)
    
### Grab Info
### [ADB Mode] - Get device Name / Module / Product Version / Chip Info
def adb_os_mode_info(list):
  
    print("[Name]:")
    project_name = "adb -s " + list + " ---Critical info that can't show here--- "
    os.system(project_name)
    print()
    
    print("[Module]:")
    module = "adb -s " + list + " ---Critical info that can't show here--- "
    os.system(module)
    print()
    
    print("[Product Version]:")
    product_version = "adb -s " + list + " ---Critical info that can't show here--- "
    os.system(product_version)
    print()
    
    print("[Chip info]:")
    chip_info = "adb -s " + list + " ---Critical info that can't show here--- "
    os.system(chip_info)
    print()
    
    ### Change mode to fastboot mode
    mode_to_fastboot = "adb -s " + list + " reboot bootloader"
    os.system(mode_to_fastboot)
    
### [Fastboot Mode] - Get Secureboot Status / <*** id> / <*** serial>
def fastboot_mode_info(list):
  
    print("[Secureboot Status]:")
    secureboot_statsu = "adb -s " + list + " ---Critical info that can't show here--- "
    os.system(secureboot_statsu)
    print()
    
    print("[*** id]:")
    <***_id> = "adb -s " + list + " ---Critical info that can't show here--- "
    os.system(<***_id>)
    print()
    
    print("[<*** serial>]:")
    <***_serial> = "adb -s " + list + " ---Critical info that can't show here--- "
    os.system(<***_serial>)
    print()
    
    ### Change mode to os mode
    mode_to_os = "fastboot -s " + list + " reboot"
    os.system(mode_to_os)
    
### Main code
### [ADB Mode]
adbsn = _List("adb devices")

for i in range (len(adbsn)):
    print(adb_root(str(adbsn[i])))
    print("\n"+"\033[1m"+"Devices information under OS Mode: "+"\033[0m")
    print("\n"+"[SN]:")
    print(adbsn[i])
    print()
    print(adb_os_mode_info(str(adbsn[i])))
    print("\n")
    
time.sleep(4)

### [Fastboot Mode]
fastbootsn = _List("fastboot devices")

for i in range (len(fastbootsn)):
    print("\n"+"\033[1m"+"Devices information under Fastboot Mode: "+"\033[0m")
    print("\n"+"[SN]:")
    print(fastbootsn[i])
    print()
    print(fastboot_mode_info(str(fastbootsn[i])))
    
