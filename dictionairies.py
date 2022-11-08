# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 14:20:28 2022

@author: nelso

Title: dictionaries
Status: on going
"""

"""
Quick Reference D = {} creates an empty dictionary
D = {key1:value1, ...} creates a non-empty dictionary
D[key] returns the value thats mapped to by key. (What if there’s no such key?)
D[key] = newvalue maps newvalue to key. Overwrites any previous value. Remember - newvalue can be any valid Python data structure.
del D[key] deletes the mapping with that key from D.
len(D) returns the number of entries (mappings) in D.
x in D, x not in D checks whether the key x is in the dictionary D.
D.keys() - returns a list of all the keys in the dictionary.
D.values() - returns a list of all the values in the dictionary.

 


For this exercise, write a dictionary that catalogs the classes you took last term - the keys should be the class CRN number (without the 'CRN' part), and the values should be the title of the class.

Then, write a function 'add class' that takes 2 arguments 
- a class number and a description 
- and adds the class to your dictionary.  Use this function to add the classes you’re taking this term to the dictionary.

Finally, write a function print classes that takes one argument
 - a Course CRN number  
 - and prints out all the classes you took in that have that CRN or a smaller CRN.


Example output:

>> print_classes(’77693’)


Introduction to Python

if you input a CRN that is not in your dictionary, say 
>> print_classes(’99999’) The print the message: 

No Course 99999 classes taken.

For this exercise,  the key can be a number and the values a string. Be sure to test with Course numbers that you both did, and did not take! 
"""


dict = {52075:'US history from 1865', 53096:'history of hip hop', 75294:'phys 120', 74599:'math 220', 77693:'cis 177 intro to python', 71326:'weld 101 welding' }
print(dict)


def addclass(dict):
    crn = input()
    name = input()
    tempdict = {crn:name}
    dict.update(tempdict)
    
    
    
def findclasses(crn):
    
    length= len(dict)# lists the size of the dictionary
    print("legnth of the dictionary is ",length)
    
    lkeys =[]
    lkeys = dict.keys()
    print("crn is",crn)
    print("these are the keys",lkeys,"\n")
    
    
    if crn not in lkeys:
        print("never took that class")
        return ("never took that class")
    
    else:
        for x in lkeys:
              
            if x <= crn:
                
                print(x,dict.get(x))
    
 

findclasses(74599)

























"""
 tempdict = dict.items()
 
 length= len(tempdict)
 
 for x in range(0,length):
     
     if crn == tempdict.index(x):
         
         print(tempdict.index(x))
         
     elif crn > tempdict.index(x):
         
         print(tempdict.index(x))"""











"""for x in range(0,length):
    
    if crn in dict:
        
        dicttemp = dict.index(x)
        
        tempcrn = dicttemp.keys()
        
        for x in range(0,length):
            
            dictkey = dict.get(x)
            
            if dictkey < tempcrn:
                
                print(dict.index[x].values())
                
        print(dict.index[x])"""



