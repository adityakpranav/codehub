class Trie:

    def __init__(self):
        self.trie = {}
    def insert(self, word: str) -> None:
        word = word + "$"
        self.addToTrie(word,self.trie)        

    def search(self, word: str) -> bool:
        word = word + "$"
        return (True if self.findInTrie(word,self.trie)>0 and self.len==1 else False)
        

    def startsWith(self, prefix: str) -> bool:
        return (True if self.findInTrie(prefix,self.trie)>0  else False)
        

    def addToTrie(self,item,dict):
        if len(item) == 0:
            pass
        else:
            if item[0] in dict:
                dict[item[0]]["co"]+=1
            else:
                dict[item[0]]={"co":1}
            #dict.setdefault(item[0],{0})
            self.addToTrie(item[1:],dict[item[0]])
    

    def findInTrie(self,ser,dict):
        self.len = -1
        #print(ser,json.dumps(dict,indent=4))
        if len(ser)==0:
            return(0)

        elif len(ser)==1 and ser in dict:
            self.len =1 if dict.get("$") is not None else 0 
            return((dict[ser]["co"]))

        else:
            if ser[0] in dict:
                
                return(self.findInTrie(ser[1:],dict[ser[0]]))
            else:
                return(0)

trie = Trie();

print(trie.insert("apple"))
print(trie.search("apple"))   # returns true
print(trie.search("app"))    # returns false
print(trie.startsWith("app")) # returns true
trie.insert("app")   
print(trie.search("app"))     # returns true

import json
print(json.dumps(trie.trie,indent=2))