import random

someList = [random.randint(0, 100) for i in range(random.randint(5, 50))]

def printList(oneList):
    for elem in oneList:
        print(elem, end=' ')
    print()

def searchList(oneList, x):
    flag = False
    for elem in oneList:
        if elem == x:
            flag = True
            return True, oneList.index(elem)
    if not flag:
        return False

def removeElemList(oneList):
    for elem in oneList:
        if oneList.count(elem) != 1:
            for i in range(oneList.count(elem)):
                oneList.remove(elem)

def sortList(oneList):
    for i in range(len(oneList)):
        for j in range(len(oneList) - 1):
            if oneList[j] > oneList[j + 1]:
                buf = oneList[j + 1]
                oneList[j + 1] = oneList[j]
                oneList[j] = buf

printList(someList)
print(searchList(someList, int(input())))
removeElemList(someList)
printList(someList)
sortList(someList)
printList(someList)