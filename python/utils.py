def countElementInList(elementList, element):
    count = 0

    for i in range(len(elementList)):
        if(elementList[i] == element):
            count += 1

    return count