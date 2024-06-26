import os
import datetime
import linecache
import colorama
from colorama import Fore, Back
import glob

colorama.init()

global start

global user

orange = '\x1b[38;2;255;165;0m'

def MonoType():
    print("Welcome to EvanRunnerStudios (TM) MonoType")




def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    MonoType()

#This makes all text orange
print(orange)

#ui stands for user input
global ui
#this is the commands list that stores all the commands
global page1
page1 = "\ntime\nfile txt read\nfile create [filename]\nrun\nfile list\nfile delete [filename]\ncustom commands\nclear\n"
page2 = "\nfile create&edit [filename]\nconfig"

global message
def ERROR(message):
    print(Back.RED + Fore.WHITE + f"ERROR: {message}" + orange + Back.RESET)
    print(orange)


def system():
    clear()
    print("Type help for a list of commands!\n")

    #this is for if the system is running
    global run
    run = True
    
    while run:

        user = linecache.getline('user.txt', 1).strip(' ').strip('\n')
        

        time = datetime.datetime.now()


        ui = input(f'MonoType#{Fore.BLUE}{user}{orange}~ ').lower()


        if ui == "help":
            print(page1)
            print("type help2 for page 2\n")
        if ui == "help2":
            print(page2)
            print("type help3 for page 3\n")
        if ui == "time":
            print(f"The the current date and time is: {time}")
        if ui.startswith("file txt read "):
            ui = ui.strip('file txt read ')
            lr = ui
            fileco = linecache.getline(f"{lr}.txt", 1)
            print('\n' + fileco.replace("||", "\n"))
        if ui.startswith("file create&edit "):
            ui = ui.strip('file create&edit ')
            ln = ui

            li =  input("type in the file || to create a new line: ")

            with open(f"{ln}.txt", "w") as file:
                file.write(li)

        if ui.startswith("file create "):
            ui = ui.strip('file create ')
            ln = ui

            with open(f"{ln}.txt", "w") as file:
                 pass
    
        if ui.startswith('run basicpy '):
            ftr = ui.strip('run basicpy ')
            try:
                with open(f"{ftr}.txt", "r") as file:
                    python_code = file.read().replace("||", "\n")
                    exec(python_code)
            except:
                print(Back.RED + Fore.WHITE + "ERROR IN COMPILING" + orange + Back.RESET)
                print(orange)
        if ui.startswith("file list") or ui.startswith("fls"):

            # List all files in the current directory
            files = glob.glob('*.*')

            print("\nListing All Files...\n")

            # Print the list of files
            for file in files:
                print(file)
            print('\n')

        if ui.startswith('file delete '):
            wftd = ui.strip('file delete ')
            #this stands for what file to delete
            try:
                os.remove(f"{wftd}.txt")
                if wftd == "[cc]":
                    print(Back.RED + Fore.WHITE + "\n\nERROR CC NOT FOUND:\nPOWER OFF YOUR SYSTEM THEN POWER BACK ON TO GET CC BACK ITS A REQUIRED FILE\n\n" + orange + Back.RESET)
                    print(orange)
            except FileNotFoundError:
                print(Back.RED + Fore.WHITE + "ERROR THIS FILE DOES NOT EXIST" + orange + Back.RESET)
                print(orange)
            except PermissionError:
                print(Back.RED + Fore.WHITE + f"ERROR NO PERMISSION: CANT DELETE {wftd}" + orange + Back.RESET)
                print(orange)
            except:
                print(Back.RED + Fore.WHITE + "AN UNKNOWN ERROR OCCURED" + orange + Back.RESET)
                print(orange)

        if ui.startswith(': '):
            ui = ui.strip(': ')
            try:
                os.system(ui)
            except:
                print(Back.RED + Fore.WHITE + "ERROR: THIS IS NOT A COMMAND" + orange + Back.RESET)
                print(orange)
            
        if ui.startswith('custom commands'):
            print("\nMonoType is a terminal based os made in python and can execute python code")
            print("MonoType also is linux based if your running this as your os it has it an boots it automatically")
            print("MonoType is made by Evan Runner Pason as an online alias")
            print("MonoType has Some Important features you can utilize such as custom commands if this file is not already there")
            print("you can create it yourself do filecreate the file name is cc for custom commands then you can write in that file")
            print("for the first line write the ammount of custom commands you will be using then like 1 or 2 then do || for the next line")
            print("then write the file that you want to cc to run simple as that you do NOT NEED TO PUT THE FILE EXTINSION you will most likely")
            print("NEVER NEED TO DO THAT IN MonoType OS because all files are .txt but then compile to other file types the custom command")
            print("is going to be the files name so now you can type the files name and it will run automatically as a command\n")

        if ui == "clear":
            clear()

        if ui.startswith("say "):  # Check if the input starts with 'say'
            ui = ui.strip('say ').replace('[user]', Fore.BLUE + user + orange).replace('||', '\n').replace('orange*', orange).replace('red*', Fore.RED).replace('blue*', Fore.BLUE).replace('yellow*', Fore.YELLOW)
            print(ui)  # Output the remaining part of the string
        
        if ui.startswith("update user"):
            user = linecache.getline('user.txt', 1).strip(' ').strip('\n')
            password = linecache.getline('user.txt', 2).strip(' ').strip('\n')
        
        if ui.startswith('system off'):
            try:
                os.system('sudo shutdown -h now')
            except:
                ERROR('YOU MAY BE RUNNING THIS IN A EMULATOR OR ARE NOT USING LINUX DEBIAN')

        if ui.startswith('system reboot'):
            try:
                os.system('sudo shutdown -r now')
            except:
                ERROR('YOU MAY BE RUNNING THIS IN A EMULATOR OR ARE NOT USING LINUX DEBIAN')


        
        

            



        #THIS IS FOR THE HELP COMMANDS OF THE COMMANDS

        #THIS IS FOR THE CUSTOM COMMANDS

        #ccl stands for custom command lines lines

        # Read the number of custom commands from the file

        try:
            ccl = int(linecache.getline('[cc].txt', 1).strip())
            customcommands = []

            # Load custom commands from the file
            for i in range(ccl):
                command = linecache.getline('[cc].txt', i + 2).strip()  # Read and strip newlines and whitespace
                customcommands.append(command)

            if ui in customcommands:
                try:
                    # Open the corresponding command file and execute its Python code
                    with open(f"{ui}.txt", "r") as file:
                        python_code = file.read().replace("||", "\n")
                        print('\n')
                        exec(python_code)
                except:
                    # If there's an error, print it with colors for visibility
                    print(Back.RED + Fore.WHITE + "ERROR IN COMPILING" + orange + Back.RESET)
                    print("\n")
        except:
            print(Back.RED + Fore.WHITE + "ERROR WITH CUSTOM COMMANDS: FIX DELETE cc" + orange + Back.RESET)
            print("\n")
            

def boot():
    clear()
    print("BOOTING...")
    file_path = '[cc].txt'
    files = glob.glob(file_path)
    if files:
        pass
    else:
        with open(file_path, 'w') as file:
            file.write("0")

    file_path = 'user.txt'
    files = glob.glob(file_path)
    if files:
        pass
    else:
        with open(file_path, 'w') as file:
            file.write("guest\nnone")
    system()
            
#This is the main function
boot()
