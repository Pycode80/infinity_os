##### -- IMPORT SECTION -- #####
import login
import prompt
import clear
import os


##### -- PRESENTATION SECTION -- #####
print("""
██╗███╗░░██╗███████╗██╗███╗░░██╗██╗████████╗██╗░░░██╗  ░█████╗░░██████╗
██║████╗░██║██╔════╝██║████╗░██║██║╚══██╔══╝╚██╗░██╔╝  ██╔══██╗██╔════╝
██║██╔██╗██║█████╗░░██║██╔██╗██║██║░░░██║░░░░╚████╔╝░  ██║░░██║╚█████╗░
██║██║╚████║██╔══╝░░██║██║╚████║██║░░░██║░░░░░╚██╔╝░░  ██║░░██║░╚═══██╗
██║██║░╚███║██║░░░░░██║██║░╚███║██║░░░██║░░░░░░██║░░░  ╚█████╔╝██████╔╝
╚═╝╚═╝░░╚══╝╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═╝░░░╚═╝░░░░░░╚═╝░░░  ░╚════╝░╚═════╝░
NB : The default admin account is root:root.
If this is your first time using the operating system,
you must log in as root to create a user.
""")

print("Please log in to access your account : ")
login_function_return = login.login()
if login_function_return[0] == True:
    username = login_function_return[1]
    clear.clear()
    while True:
        current_path = os.getcwd()
        command = input(username+"@infinityos:"+current_path+"$ ")
        prompt.execute(command)
    
    
else:
    print("An error occured, exiting...")