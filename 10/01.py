# Python Module 
#  now in this program we will import py file which is saved john.py

import john
john.x
john.add(11,22)
john.product(10,10)

# from import 

from john import add,product

add(11,11)
product(5,5)

# renameing a module at the time of import(module aliasing )

import john as j

j.product(11,11)


# Various possibilities of import 
# import module1,module2,mnodule3
# import module1 as m1, module2 as m2


# The Special Variable __name__:
# for every python program, a special variable __name__ will be added internally. 
# This variables stores information regarding wheather the program is execute as an 
# indivisual program or as a module 

# if the program executed as an indivisual program then the value of this variable is __main__ 





