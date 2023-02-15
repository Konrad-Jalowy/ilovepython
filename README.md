# ilovepython

## Notes on this project:
- **check if you have venv(linux):**
```sh
virtualenv --version
```
- **insall pip and venv in necessary (ubuntu):**
```sh
sudo apt-get install python-pip
```
```sh
pip install virtualenv
```
- **create venv (linux):**
```sh
virtualenv virtualenv_name
```
- **activate venv (linux):**
```sh
source virtualenv_name/bin/activate
```
- **deactivate venv:**
```sh
deactivate
```
- **install argparse library:**
```sh
pip install argparse
```
- **create argument --do**
```py
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--do', type=str, required=False)
args = parser.parse_args()
```
- **use argument do in code**
```py
if args.do is not None:
    command = args.do
    mainloop(command)
else:
    mainloop()
```
- **use argument do in shell:**
```sh
python main.py --do="help"
```
```sh
python main.py --do=help
```
```sh
python main.py --do help
```
```sh
python main.py --do "help"
```
- **simple correction of user input:**
```py
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
def get_description(ipt):
    if not ipt.startswith("/"):
        ipt = "/" + ipt
    if ipt not in explanations:
        print("Unknown location")
    else:
        print(ipt + ": " + explanations[ipt])
```
- **how to iterate over python dictionary with keys, values and indexes:**
```py
def print_all():
    print("Available locations:")
    for idx, (key, value) in enumerate(explanations.items()):
        print(f"{idx+1}: {key} - {value}")
```
```py
commands = {
    "q/Q/quit": "Quit the program",
    "h/H/help": "Show help",
    "a/A/all" : "List All",
    "/location_name" : "Show description"
}
def print_help():
    print("Available commands:")
    for idx, (key, value) in enumerate(commands.items()):
        print(f"{idx+1}: {key} - {value}")
```
- **python match case (with | operator) - great new Python feature (get new Python!!!!):**
```py
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
```
- **Note to myself: I learned today that you cannot break out of the loop from within function called inside that loop. But you can return some value or change some flag to break out of it. Here is mainloop in this mini-project as for now:**
```py
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
```
## App
- **Very simple app to help me learn linux FSH (Filesystem Hierarchy Standard)**
- **A little messy but I have little time and learning a lot of different stuff. I will make it better**
- **If I have any time, i will do some changes. TODOS:**
    - **Add other topics**
    - **Make it OOP**
    - **use some persistent storage for definitions and add function to add new definitions**
    - **maybe some GUI in future?**

## My Rant
- **I really love Python. I have a problem though with presenting it as a great language for beginners**
- **All simple hello worlds aside, when a beginner encounters OOP in Python or frameworks he gets confused**
- **OOP in Python and most languages is very different. Multi-inheritance, decorators (not as a design pattern), lack of access modifiers... You cannot learn OOP fully in my opinion**
- **Python is great for people with some background. Math background, network/linux background, data science background. When you begin coding not knowing anything there isnt much you can do in Python**
- **Python is too abstracted away from CS and if you know nothing about CS, if thats how you start, you have a really hard time to understand it all**
- **JS and PHP are languages, that in my opinion, are great not only because of what can do, but because you can actually learn a lot and fill the gaps, whatever they might be (like how HTTP works, how client-server works, everything you dont know) while in Python you "write like English", "read like English", but you dont feel any confidence in your CS skills**
- **Another great languages for learning purposes are Java/C# (for OOP, best for OOP), TS (best way to learn generics, decorators) and basic C (like memory management, pointers, no big projects)**
- **Some people think, like me, that when they are CS noobs and dont feel good about their skills coding in Python, that learning C++ is a good idea. Been that way before. Its not:**
    - **OOP in C++ exists, but it is so... IDK, obfuscated, that you should learn Java or C# instead. Its easier to learn OOP in Visual Basic than in C++. C++ is so packed with features that should be divided and learned separately that...**
    - **To get the idea how pointers work, how some low level stuff works, its better to just try C**
    - **A lot of strongly-typed stuff can be learned easier in TS. Idk why, but its easier to get it in TS**
- **Python is great, but when youre beginner, you hate any problems, errors, that scare you away. And in Python either you use windows, Pycharm, it creates venv, if you even notice it and start using pip, great, but you will always have some issue with some library bc on tutorial everything works but on your localhost it doesnt. You will find a thread and 5 solutions, none of them works for you.**
- **You can use linux. Just dont get confused with python, python3, creating your own venv and so on. Seems obvious, but for beginner with no CS background it is hard and scary. Python is great, will try to do more stuff with it in future, its especially great at scripting, but... having learned Python as my first language, I would not recommend it for beginners, no matter how easy Python hello worlds might seem**