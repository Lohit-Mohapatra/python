Insertion Sort
--------------
Insertion sort divides the list into 2 subsets - sorted and unsorted.
Initially only one element is present in the sorted subset at index 0 and for each iteration, the insertion sort removes the next element from unsorted subset, finds the location it belongs within the sorted subset and then inserts it at that place. 
This goes on till there are no more input elements remaining.

def insertionSort(nlist):
   for index in range(1,len(nlist)):

     currentvalue = nlist[index]   
     position = index
     
     while position>0 and nlist[position-1]>currentvalue:
         nlist[position]=nlist[position-1]   
         position = position-1
        
     nlist[position]=currentvalue

nlist = [14,46,43,27,57,41,45,21,70]
insertionSort(nlist)
print(nlist)


Selection Sort
--------------
The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning

arr = [10,9,7,6,5,4,12,32,43,29]
def selectionSort(arr):
    for i in range(len(arr)):
        min_idx=i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx=j
                
        arr[min_idx], arr[i] = arr[i], arr[min_idx]  
        
selectionSort(arr)
print(arr)


Bubble Sort
-----------
Bubble Sort works by repeatedly swapping the adjacent elements if they are in wrong order.

arr = [10,9,7,6,5,4,12,32,43,29]
def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
               arr[j], arr[j+1] = arr[j+1], arr[j]
            
bubbleSort(arr)
print(arr)    



Difference between BubbleSort, InsertionSort and SelectionSort :
Bubble sort repeatedly compares and swaps(if needed) adjacent elements in every pass. 
Selection sort takes the current element and exchange it with the smallest element on the right hand side of the current element.
Insertion sort take the current element and insert it at the appropriate position of the list, adjusting the list every time you insert. It is similar to arranging the cards in a Card game.
