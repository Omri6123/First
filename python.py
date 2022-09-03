def are_lists_equal(list1, list2):
    if(sorted(list1) ==sorted(list2)):
        return True
    return False

def longest(mylist):
    mylist.sort(key=len)
    return mylist[-1]

def try_update_letter_guessed(letter_guessed, old_letter_guessed):
    if ((letter_guessed in old_letter_guessed)):
        old_letter_guessed.sort()
        badstring = ""
        for i in range (len(old_letter_guessed)):
            badstring = badstring + old_letter_guessed[i] + " -> "
        badstring = badstring[0:len(badstring)-4]
        print("X\n" + badstring + "\nFalse" )
    else:
        old_letter_guessed.append(letter_guessed)
        print("True")

from dataclasses import replace
from fnmatch import translate
import math
def squared_numbers(start, stop):
    squarelist = []
    while(start <= stop):
        squarelist.append(int(math.pow(start, 2)))
        start+= 1
    return squarelist


def is_greater(my_list, n):
    newlist = []
    for item in my_list:
        if(item > n):
            newlist.append(item)
            
    return newlist

def numbers_letters_count(my_str):
    newlist = [0,0]
    for item in my_str:
        if(item >='0' and item<='9'):
            newlist[0] += 1
        else:
            newlist[1] +=1
    return newlist

def seven_boom(end_number):
    newlist = []
    for i in range(end_number +1):
        newlist.append(i)
    for i in newlist:
        if('7' in str(i)):
            newlist[i] = "BOOM"
    return newlist

def sequence_del(my_str):
    newstr = ""
    for i in range(1, len(my_str)):
        if(my_str[i] != my_str[i-1]):
             newstr += my_str[i-1]
    newstr+= my_str[len(my_str)-1]
    return newstr

def GroceryListfunction(grocerystring):
    num = input("Enter a number between 1-9")
    Grocerylist= grocerystring.split(',')
    while(num != 9):
        if(num==1):
            for i in Grocerylist:
                print(i)
        elif(num==2):
            count = 0
            for i in Grocerylist:
                    count+=1
            print("There are " + count + " grocceries in the list")
        elif(num==3):
            item = input("Enter a gorcery")
            if(item in Grocerylist):
                print("The item is in the grocery list")
            else:
                print("The item isn't in the gorcery list")
        elif(num==4):
            item = input("Enter a gorcery")
            count = 0
            for i in Grocerylist:
                if(item == i):
                    count+=1
            print("The grocery appears " + count + " times in the list")
        elif(num==5):
            item = input("Enter a gorcery")
            Grocerylist.remove(item)



#old_letters = ['a', 'p', 'c', 'f']
#print(sequence_del("Heeyyy   yyouuuu!!!"))
#print(squared_numbers(-3,3))
grocery = ["niv", "omri", "niv", "omri"]
grocery.remove("niv")
print(grocery)
#try_update_letter_guessed('s', old_letters)
#try_update_letter_guessed('b', old_letters)
#try_update_letter_guessed('b',old_letters)