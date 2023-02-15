import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--do', type=str, required=False)
args = parser.parse_args()

def mainloop(arg=None):
    while True:
        if arg:
            flag = match_command(arg)
            arg = None
            if flag == -1:
                print("Bye")
                break
        else:
            command = input("What do you want me to explain? > ")
            flag = match_command(command)
            if flag == -1:
                print("Bye")
                break


explanations = {
    "/bin" : "stores essential command-line utilities and binaries",
    "/boot" : "stores files to boot your linux system",
    "/dev" : "hardware/software drivers",
    "/etc" : "basic conf files",
    "/home" : "home dirs for the users",
    "/lib": "shared libraries",
    "/media": "mount points for CD, floppy and other removable media",
    "/mnt": "temp mount for filesystem",
    "/proc": "kernel information",
    "/usr" : "readonly stuff accessible to users",
    "/root" : "root directory",
    "/sys" : "info about devices",
    "/sbin" : "binaries for boot, root etc... essential binaries in /bin",
    "/tmp" : "self-decriptive" 
}
commands = {
    "q/Q/quit": "Quit the program",
    "h/H/help": "Show help",
    "a/A/all" : "List All",
    "/location_name" : "Show description"
}
def match_command(command):
    match command.lower():
        case "q" | "quit":
            return -1
        case "all" | "a":
            print_all()
        case "help" | "h":
            print_help()
        case other:
            get_description(command)

def print_all():
    print("Available locations:")
    for idx, (key, value) in enumerate(explanations.items()):
        print(f"{idx+1}: {key} - {value}")
def print_help():
    print("Available commands:")
    for idx, (key, value) in enumerate(commands.items()):
        print(f"{idx+1}: {key} - {value}")

def get_description(ipt):
    if not ipt.startswith("/"):
        ipt = "/" + ipt
    if ipt not in explanations:
        print("Unknown location")
    else:
        print(ipt + ": " + explanations[ipt])


if args.do is not None:
    command = args.do
    mainloop(command)
else:
    mainloop()
    

