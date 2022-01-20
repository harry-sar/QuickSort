import time, random

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

def validation(data_array):
    check=None
    for x in data_array:
        if type(x) not in [type(0),type(0.0)]:
            check=False
    if check==False:
        return []
    else:
        return data_array

def run_sort(dataArray):
    lowPoint=0 #starting index
    highPoint=len(dataArray)-1 # last index
    dataArray = validation(dataArray)
    if dataArray!=[]:
        quickSort(dataArray, lowPoint, highPoint)
        print(dataArray)
    else:
        print("Invalid Array Data")

if __name__ == "__main__":
    # [7, 9, 10, 4, 1, 3, 0, 2, 6, 5, 8, ]
    list_random=[random.randint(1,10000000) for x in range(1000)]
    st = time.time()
    run_sort(list_random)
    print(f"Time Taken is {'{:f}'.format(time.time()-st)} Seconds!")


