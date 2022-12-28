import threading 

def merge_sort(array):
  if len(array)==1:
    return(array)
  else:
     mid=len(array)//2

     L= array[:mid]
     R= array[mid:]

     merge_sort(L)
     merge_sort(R)

     i = j = k = 0
     while i < len(L) and j < len(R):
       if L[i] < R[j]:
         array[k] = L[i]
         i += 1
       else:
         array[k]=R[j]
         j+=1
       k+=1
     while i < len(L):
       array[k] = L[i]
       i += 1
       k += 1
     while j < len(R):
       array[k] = R[j]
       j += 1
       k += 1
array=[]
n=int(input("Number of elements in array:"))
for i in range(0,n):
   l=int(input())
   array.append(l)
print("Unsorted array:", array)
merge_sort(array)
print("Sorted array:",array)
t1 = threading.Thread(target=merge_sort, args=(array,))  
t2 = threading.Thread(target=merge_sort, args=(array,))  

t1.start()

t2.start()

t1.join()
t2.join()
print("done")
