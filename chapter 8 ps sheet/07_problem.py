'''def rem(l,word):
    for item in l:
        l.remove(word)
        return l


l = ["alain" , "landary", "mang", "an"]

print(rem(l,"an")) '''



def rem(l,word):
    n =[]
    for item in l:
       if not(item == word):
         n.append(item.strip(word))
    return n


l = ["landary", "Rohan", "an"]

print(rem(l, "an" ))