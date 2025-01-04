import random
import time


# Implementation of Binary Search Algorithm 

#We will prove that binary search is better than naive Search
# naive search  : scan entire list and ask if tarhet is equal
#if yes : return index 
#if no : then return -1

def naive_search(l , target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

def binary_search(l , target , low=None , high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low :
        return -2

    #example l = [1,2,5,10,12] # target =10 should return 3
    midpoint = (low + high) // 2

    if l[midpoint] == target:
        return midpoint

    elif target < l[midpoint]:
        return binary_search(l , target , low , midpoint -1)

    else:
                return binary_search(l , target , midpoint+1 , high)


if __name__ == '__main__':
    l = [1,3,5,10,12]
    target = 10
    print(naive_search(l,target))
    print(binary_search(l,target))

    """
        To check which search is better and takes less time for searching
    """   
    # length = 10000
    # #build a sortef list of length 10000
    # sorted_list = set()
    # while len(sorted_list) < length:
    #     sorted_list.add(random.randint(-3*length , 3* length))

    # sorted_list = sorted(list(sorted_list))

    # start = time.time()
    # #To iterate every single item in list
    # for target in sorted_list:
    #     naive_search(sorted_list , target)

    # end = time.time()
    # print("Naive search Time :" , (end - start)/length, "seconds")

    # start = time.time()
    # #To iterate every single item in list
    # for target in sorted_list:
    #     binary_search(sorted_list , target)

    # end = time.time()
    # print("Binary search Time :" , (end - start)/length, "seconds")
