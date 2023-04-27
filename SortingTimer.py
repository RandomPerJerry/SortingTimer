# Jerry Zhang
# Sorting Timer

import random, time

# This generates a list that contains 10000 random integers between 0 and 100000
def get_list():
    random_list = []

    for _ in range (10000):
        random_list.append(random.randint(0, 10000))

    return random_list

#bubble sort algorithem
def fnBubble(RList):
    #Pre: enter a list that contains only integer
    #post: using bubble sort to sort the list from small to big

    ln = len(RList)

    for i in range(ln) :
        swap = False

        #the amount of numbers it needed to check decreases every one round
        for j in range(ln - i - 1) :
            
            #swap places if the number to its right is smaller
            if RList[j] > RList[j + 1] : 
                RList[j], RList[j + 1] = RList[j + 1], RList[j]
                swap = True

        # when there is no swap in a run through or i reached len(RList), the loop ends
        if not swap:
            break
    
    #return sorted list
    return RList

def fnSelection(RList):
    ln = len(RList)
    # Pre: enter a list that contains only integer
    # post: using selection sort to sort the list from small to big
    
    # loop over the list up to the second to last element
    for i in range(ln - 1):
        # Assume the current index is the minimum
        iMIn = i

        # Iterate over the unsorted part of the list
        for j in range(i + 1, ln):
            # If we find a smaller element, update the index of the minimum
            if RList[j] < RList[iMIn]:
                iMIn = j

        # If the minimum is not at the current index, swap the elements
        if iMIn != i:
            RList[i], RList[iMIn] = RList[iMIn], RList[i]

    # Return the sorted list
    return RList


def fnInsertion(RList):
    # Pre: enter a list that contains only integer
    # post: using Insertion sort to sort the list from small to big

    ln = len(RList)

    # Iterate over the list starting from the second element
    for i in range(1, ln):
        # Store the current element as the target
        target = RList[i]
        # Set the comparison index to the previous element
        j = i - 1
    
        # loop over the sorted part of the list backwards
        while j >= 0 and target < RList[j]:
            # If the target is smaller than the current element, move the element to the right to make room for the target
            RList[j + 1] = RList[j]
            # Move the comparison index one position to the left
            j = j - 1
        
        # Insert the target in its correct position in the sorted part of the list
        RList[j + 1] = target

    # Return the sorted list
    return RList

def fnQuickSort(RList):
    # Pre: enter a list that contains only integer
    # post: using quick sort to sort the list from small to big

    # If the array is empty or has only one element, it is already sorted
    if len(RList) <= 1:
        return RList

    # Choose a pivot element from the middle of the array
    pivot = RList[len(RList) // 2]

    # Create three new lists to hold elements less than, equal to, and greater than the pivot
    left = [x for x in RList if x < pivot]
    middle = [x for x in RList if x == pivot]
    right = [x for x in RList if x > pivot]

    # Recursively sort the left and right lists using the same quick sort algorithm
    # and then concatenate them with the middle list to get the final sorted array
    return fnQuickSort(left) + middle + fnQuickSort(right)



def fnBinarysearch(sortedlist, target):
    # Initialize left and right pointers to the start and end of the list respectively
    left = 0
    right = len(sortedlist) - 1

    # Initialize count to keep track of how many times the function accesses the list
    count = 0

    # Loop until the left and right pointers cross each other
    while left <= right:
        # Increment count for each iteration of the loop
        count += 1

        # Calculate the mid-point index
        mid = (left + right) // 2

        # If the target is found at the mid-point index, return the index and the count
        if target == sortedlist[mid]:
            return mid, count

        # If the target is greater than the mid-point element, discard the left half of the list
        elif target > sortedlist[mid]:
            left = mid + 1

        # If the target is smaller than the mid-point element, discard the right half of the list
        else:
            right = mid - 1

    # If the target is not found in the list, return None and the count
    return None, count




def fnDisplay():
    # Pre: none
    # Post: Generates a 10,000 int list, times how long it takes for each sorting algorithm to sort the list,
    #       and returns the time and the sorted list.

    RList = get_list()

    # Time how long it takes for each sorting algorithm to sort the list.
    BubbleS = time.time()
    BubleList = fnBubble(RList[:])
    BubbleF = time.time()

    SelectionS = time.time()
    SelectionList = fnSelection(RList[:])
    SelectionF = time.time()

    InsertionS = time.time()
    InsertionList = fnInsertion(RList[:])
    InsertionF = time.time()

    QuickS = time.time()
    QuickList = fnQuickSort(RList[:])
    QuickF = time.time()

    # Display the result in the correct format.
    DisplayResult = f"Original List of 10,000 numbers: ({', '.join(map(str, RList[:5]))} ... {', '.join(map(str, RList[-5:]))})\n\n" \
                    f"Bubble Sort: ({', '.join(map(str, BubleList[:5]))} ... {', '.join(map(str, BubleList[-5:]))}) took {BubbleF - BubbleS} seconds\n" \
                    f"Selection Sort: ({', '.join(map(str, SelectionList[:5]))} ... {', '.join(map(str, SelectionList[-5:]))}) took {SelectionF - SelectionS} seconds\n" \
                    f"Insertion Sort: ({', '.join(map(str, InsertionList[:5]))} ... {', '.join(map(str, InsertionList[-5:]))}) took {InsertionF - InsertionS} seconds\n" \
                    f"Quick Sort: ({', '.join(map(str, QuickList[:5]))} ... {', '.join(map(str, QuickList[-5:]))}) took {QuickF - QuickS} seconds\n"
    # Return the result and the sorted list.
    return DisplayResult, QuickList


#Catches the result
resultdisplay, sorted_list = fnDisplay()

#print out the result
print(resultdisplay)

#ask the user what int they want to find in the sorted list
user_target = int(input("Enter the number you want to find: "))

#Get the index of the user-requested number and how much checks it took
Numberindex, numberchecks = fnBinarysearch(sorted_list, user_target)

#print out the result in format
if Numberindex == None:
    print(f"The number you requested does not exist in this list, it took {numberchecks} number checks to figure this out")
else:
    print(f"The index of the number you want to find is {Numberindex}, it took {numberchecks} number checks")