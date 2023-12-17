def byRef(myList2):
    print('\nThe received list2 is: ',  myList2)
    myList2.append([1, 2, 3])

    print('in byRef the list2 is : ', myList2)


def callingF():


    myList = [20, 30, 40]

    print('The list in the calling function is: ', myList)

    byRef(myList)

    print('\nIn the calling function the list is:', myList)

callingF()

