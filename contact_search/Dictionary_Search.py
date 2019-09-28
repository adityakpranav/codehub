'''

'''

import json

def addToTrie(item,dict):
    if len(item) == 0:
        pass
    else:
        if item[0] in dict:
            dict[item[0]]["co"]+=1
        else:
            dict[item[0]]={"co":1}
        #dict.setdefault(item[0],{0})
        addToTrie(item[1:],dict[item[0]])

def findInTrie(ser,dict):
    #print(ser,json.dumps(dict,indent=4))
    if len(ser)==0:
        print(0)
        
    elif len(ser)==1 and ser in dict:
        print((dict[ser]["co"]))
    
    else:
        if ser[0] in dict:
            findInTrie(ser[1:],dict[ser[0]])
        else:
            print(0)
    
    
Trie = {}
add = ["hack","hackerrank"]
finds = ["hac","hackerrank"]

for item in add:
    addToTrie(item,Trie)
for search in finds:
    print("\n",search,end=":")
    findInTrie(search,Trie)
    
print(json.dumps(Trie,indent=4))