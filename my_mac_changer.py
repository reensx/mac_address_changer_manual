import subprocess
import optparse
import re

def function1():

    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--interface",dest="interface",help="interface")
    parse_object.add_option("-m","--mac",dest="mac_address",help="mac address")

    return  parse_object.parse_args()



def function2(user_interface,user_mac_address):
    subprocess.call(["ifconfig",user_interface,"down"])
    subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac_address])
    subprocess.call(["ifconfig",user_interface,"up"])

def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig",interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig))

    if new_mac:
        return new_mac.group(0)
    else:
        return None


print("mac_changer started")

(user_input,arguments) = function1()
function2(user_input.interface,user_input.mac_address)
clean_mac = control_new_mac(user_input.interface)

if clean_mac == user_input.mac_address:

    print(f"your brand-new mac address {user_input.mac_address}")
    print("done!")
else:
    print("try again!")