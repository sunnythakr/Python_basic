# The Special Variable __name__:
# for every python program, a special variable __name__ will be added internally. 
# This variables stores information regarding wheather the program is execute as an 
# indivisual program or as a module 

# if the program executed as an indivisual program then the value of this variable is __main__ 



def f1():
    if __name__ =="__main__":
        print("the code executed as a program  ")
    else:
        print("the code executed as a module from some other program  ")

f1()