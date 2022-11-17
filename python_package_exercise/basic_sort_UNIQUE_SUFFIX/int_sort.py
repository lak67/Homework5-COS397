# =========================================================================
#
#  Copyright Ziv Yaniv
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0.txt
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
# =========================================================================

"""
This module sorts lists of integers...
"""


def bubble(int_list):

    # need to add parameter types
    """
    :param int_list: an unsorted list of integers
    :returns: a list of integers sorted in ascending order, the same size as int_list
    """

    n = len(int_list)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if int_list[j] > int_list[j + 1]:
                swapped = True
                int_list[j], int_list[j + 1] = int_list[j + 1], int_list[j]
         
        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return
    print("bubble sort")
    return(int_list)


def quick(int_list, low, high):
    """

    :param1 :
        int_list: list given by the user
    :param2 : 
        low: this is the first item of the array
    :param3 :
        high: this is the last item of the array
    :returns: returns the list in a sorted format from lowest to highest
    """
    if low < high:
     
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(int_list, low, high)
 
        # Recursive call on the left of pivot
        quickSort(int_list, low, pi - 1)
 
        # Recursive call on the right of pivot
        quickSort(int_list, pi + 1, high)

    print("quick sort")
    return(int_list)


def insertion(int_list):
    """
    :param int_list: 
        an unsorted list of integers
    :returns: the list of integers sorted in ascending order
    """

    # Traverse through 1 to len(arr)
    for i in range(1, len(int_list)):
 
        key = int_list[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < int_list[j] :
                int_list[j+1] = int_list[j]
                j -= 1
        int_list[j+1] = key

    print("insertion sort")
    return (int_list)

