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
