# make an automatic cypher wheel...

# extre to be done later.... ---> make it exicutable on a web browser

import re
import temp_wheel
#print (temp_wheel.ac)

# var def
x = None
y = None
z = None
fin = ("")
end  = ("")
lst = []
loop = 0


print ("notice: keep numbers and words seperate for now, still tring to figure something out for that")
x = input('MSG GOES HERE --->  ')
x = x.strip('-')


#for the cypher part, try the "white space strip" command
print("-------------------------------------------------------------------------------------------")
#make a custom call command to cycle thru each letter and put in into a new var


lst[:] = x
print (lst)


q = input('pick a number 1-3 ---------->>>  ')
# if loop using |var = len of list | and acending loop value use key in d for | letter in dict ---> if true _get letter 
y = len(lst)

if q == "1":
 while loop < y:
    z = lst[loop]
    z in temp_wheel.ab
    if True:
        fin = temp_wheel.ab.get(z)
        print (fin)
        try:
            end = end + fin
        except:
            z = lst[loop]
            end = end + z
    loop = loop + 1


if q == "2":
 while loop < y:
    z = lst[loop]
    z in temp_wheel.ac
    if True:
        fin = temp_wheel.ac.get(z)
        print (fin)
        try:
            end = end + fin
        except:
            z = lst[loop]
            end = end + z
    loop = loop + 1


if q == "3":
 while loop < y:
    z = lst[loop]
    z in temp_wheel.ad
    if True:
        fin = temp_wheel.ad.get(z)
        print (fin)
        try:
            end = end + fin
        except:
            z = lst[loop]
            end = end + z
    loop = loop + 1


print (end)