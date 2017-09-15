'''
Created on Sep 14, 2017

@author: jlearx
'''

def RemoveDupsLoop(oldlist):
    newlist = []
    [newlist.append(e) for e in oldlist if (newlist.count(e) == 0)]
    return newlist

def RemoveDupsSet(oldlist):
    newset = set(oldlist)
    return list(newset)

def GetList():
    numlist = []
    
    while (len(numlist) == 0):
        listIn = input("Please enter a list of numbers inside []: ")
        start = listIn.find("[")
        finish = listIn.find("]")
        
        if ((start >= 0) and (finish > 0) and (finish != start + 1)):
            listIn = listIn[start + 1:finish]
            listIn = listIn.replace(" ", "")
            listStr = listIn.split(",")
            numlist = listStr
            break
        
    return numlist

if __name__ == '__main__':
    oldlist = GetList()
    
    # Use a loop to remove duplicates
    newlist = RemoveDupsLoop(oldlist)
    length = len(newlist)
    
    print("Here is the list w/o duplicates using a loop:")
    
    for i in range(0, length):
        if (i < length - 1):
            print(newlist[i], end=', ')
        else:
            print(newlist[i])
    
    newlist.clear()
    
    # Use a set to remove duplicates
    newlist = RemoveDupsSet(oldlist)
    length = len(newlist)
    
    print("Here is the list w/o duplicates using sets:")
    
    for i in range(0, length):
        if (i < length - 1):
            print(newlist[i], end=', ')
        else:
            print(newlist[i])
            