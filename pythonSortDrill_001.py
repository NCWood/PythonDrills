# Python Sorting Drill
#
# Nicholas Wood (nicholas.cameron.wood@gmail.com)
#
#------------------------------------------------

def nickSort(myList1, mylist2):
    for i in range(len(myList1)-1, 0, -1):
        positionOfMax = 0
        for location in range(1,  i + 1):
            if myList1[location] > myList1[positionOfMax]:
                positionOfMax = location

        temp = myList1[i]
        myList1[i] = myList1[positionOfMax]
        myList1[positionOfMax] = temp

    for i in range(len(myList2)-1, 0, -1):
        positionOfMax = 0
        for location in range(1,  i + 1):
            if myList2[location] > myList2[positionOfMax]:
                positionOfMax = location

        temp = myList2[i]
        myList2[i] = myList2[positionOfMax]
        myList2[positionOfMax] = temp
        

myList1 = [67, 45, 2, 13, 1, 998]
myList2 = [89, 23, 33, 45, 10, 12, 45, 45, 45]
nickSort(myList1, myList2)
print(myList1)
print(myList2)
    
