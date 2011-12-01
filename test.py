'''
Created on Dec 1, 2011

@author: Bowen
'''

import re

prenoms = set()

# reconnaitre M. Sqrkozy | M. Nicolas Sarkozy, etc
regexp_1 = re.compile(r"(M|Mme|Mlle)\.\s(\b[A-Z]\w+\b)(\s\b[A-Z]\w+\b)?", re.U)

def regle_1(text):
    for n in regexp_1.finditer(text):        
        name=n.group(2)
        if n.group(3)!=None:
            name+=n.group(3)
        print name
        prenoms.add(name)
        
regle_1("M. Nicolas Sarkozy est nill et  Mlle. Alice  et Thomas")

print prenoms
