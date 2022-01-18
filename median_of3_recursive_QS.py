
def quickSort(dataArray,lowPoint,highPoint):
    '''Quick Sort implementation using Medium of three & recursion'''
    if lowPoint<highPoint:
        part = partition(dataArray,lowPoint,highPoint)
        quickSort(dataArray,lowPoint,part-1)
        quickSort(dataArray,part+1,highPoint)

def partition(dataArray,lowPoint,highPoint):
    pivot=dataArray[lowPoint]
    index = lowPoint

    while lowPoint < highPoint:
        # loop until value bigger than pivot
        while lowPoint<len(dataArray) and dataArray[lowPoint]<=pivot: #condition for left data point to increment
            lowPoint+=1

        while dataArray[highPoint]>pivot: #condition for right data point to deincrement
            highPoint-=1

        if lowPoint<highPoint:
            dataArray[lowPoint],dataArray[highPoint]=dataArray[highPoint],dataArray[lowPoint]

    dataArray[highPoint],dataArray[index]=dataArray[index],dataArray[highPoint] # swaps values in list object instead of
                                                                                # referencing new list therefore list dosent have to be
    return highPoint                                                            # returned

if __name__ == "__main__":
    dataArray=[7,9,10,4,1,3,0,2,6,5,8]
    lowPoint=0 #starting index
    highPoint=len(dataArray)-1 # last index
    quickSort(dataArray,lowPoint,highPoint)
    print(dataArray)
