import touch
import mkdir
import pwd
import clear
import cd
import ls
def execute(prompt):
    split_prompt = prompt.split(" ")
    if split_prompt[0] == "exit":
        exit()
    elif split_prompt[0] == "echo":
        print(split_prompt[1])
    elif split_prompt[0] == "touch":
        touch.touch(split_prompt[1])
    elif split_prompt[0] == "mkdir":
        mkdir.mkdir(split_prompt[1])
    elif split_prompt[0] == "pwd":
        pwd.pwd()
    elif split_prompt[0] == "clear":
        clear.clear()
    elif split_prompt[0] == "cd":
        cd.cd(split_prompt[1])
    elif split_prompt[0] == "ls":
        ls.ls()

    else:
        print("Unknow command "+split_prompt[0])


