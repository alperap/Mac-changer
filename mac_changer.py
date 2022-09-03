from optparse import OptionParser
import subprocess
import re


def user_inputs():
    inputs = OptionParser()
    inputs.add_option("-m","--mac_adress",dest="Mac_adress",help="Enter your want mac adress.")
    inputs.add_option("-i","--interface",dest="Interface",help="Enter your interface name")

    if inputs.parse_args()[0].Interface and inputs.parse_args()[0].Mac_adress:
        return inputs.parse_args()
    else:
        print("You have to enter interface or mac adress!")

def enter_values(interface,mac):
    subprocess.run(["ifconfig",interface,"down"])
    subprocess.run(["ifconfig",interface,"hw","ether",mac])
    subprocess.run(["ifconfig",interface,"up"])

def show_values(interface):
    output = subprocess.check_output(["ifconfig",interface])
    output_print = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(output))
    return output_print[0]

try:
    (key, value) = user_inputs()
    enter_values(key.Interface,key.Mac_adress)

    if show_values(key.Interface) == key.Mac_adress:
        print("Your mac adress was changed!")
    else:
        print("Try again! Unsucces")

except:
    print("Your values have to be false!")