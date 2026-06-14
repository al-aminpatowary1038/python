numList = [1,2,4,5,5,6,8,7,5,9,"ten","a","b"]
print(len (numList))
numList.append("c")
print(numList)
print(len (numList))
numList.insert(4,"three")
print(numList)
print(len (numList))
numList.remove(5)
print(numList)

numList1 = [9,1,10,4,5,15,6,50,7,5,3]
numList1.sort()
print(numList1)

numList2 = ["ten","a","b","x","r","w","d","q"]
numList2.sort()
print(numList2)

numList.reverse()
print(numList)

numList3 = numList1.copy()
print(numList3)

pos = numList3.index(5)
print(pos)

total = numList3.count(5)
print(total)