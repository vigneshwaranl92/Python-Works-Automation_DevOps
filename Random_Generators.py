from random import*
#from random import*   <-- You can do this in order to avoid typing module explicitly
import keyword



for i in range (10):
    print(randint(0,6), randint(0,20),randint(0,30),randint(1,6),randint(3,6), sep="")

print(i)


#Keyword.kwlist is used to display all the keywords which is in build in python
#According to python version3, there are 33 keywords
keyword.kwlist
