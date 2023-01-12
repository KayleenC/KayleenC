# The given script aims to easily and rapidly install the needed test APKs for our testing.
# Usage: Tap the file name "install_files.py" on your terminal.
# PoC: MyLDAP@

---------------------------------------------------------------------------

import os

def getSnList(command):
    action = os.popen(command)
    device_list = action.read()
    action.close()
    model_list = device_list.split("\n")
    return model_list

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


def parser_folder(floder_path,sufix = "*"):
    from pathlib import Path
    file_list = list(Path(folder_path).glob(f"*.{sufix}")) #*.*
    return file_list
  

### Suffix  
import argparse

parser = argparse.ArgumentParser(description = "Process some integers.")
parser.add_argument("path", help = "Insert folder path")
parser.add_argument("-r", help = "Default is 'False', switch to 'True' to run the code.", dest = "run_switch", default = "False")
parser.add_argument("-s", help = "Suffix", dest = "suffix", default = "*")


args = parser.parse_args()

folder_path = args.path
install_paths = parser_folder(floder_path,sufix=args.suffix)


### Main code [Install APK]
def install_apk(sn_list):
    cmd_string = "adb -s " + sn_list + " install"
    for install_path in install_paths:
        module = cmd_string + f"'{str(install_path)}'"
        
        if args.run_switch == "True":
            print("Installing...")
            os.system(module)
        print(module)
        print()
        #print("Install successfully!")
    print(args.run_switch)
    

adbsn_List("adb devices")

for i in range (len(adbsn)):
    print(install_apk(str(adbsn[i])))

