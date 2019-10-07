import math


def bubble_sort(l):
    n=len(l)
    for i in range(n):
        for j in range(n-1):
            if l[j]>l[j+1]:
                temp=l[j]
                l[j]=l[j+1]
                l[j+1]=temp


def selection_sort(l):
    n=len(l)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if l[min_index]>l[j]:
                temp=l[min_index]
                l[min_index]=l[j]
                l[j]=temp

def binarySearch(arr,l,r,x):
    # Check base case 
    if r >= l: 
  
        mid = l + (r - l)/2
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
          
        # If element is smaller than mid, then it  
        # can only be present in left subarray 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
  
        # Else the element can only be present  
        # in right subarray 
        else: 
            return binarySearch(arr, mid + 1, r, x) 
  
    else: 
        # Element is not present in the array 
        return -1

def main():
    l=[5,2,0,9,3]
    bubble_sort(l)
    print(l)

    l1=[5,2,0,9,3]
    selection_sort(l1)
    print(l1)

    # Test array 
    arr = [ 2, 3, 4, 10, 40 ] 
    x = 10
      
    # Function call 
    result = binarySearch(arr, 0, len(arr)-1, x) 
      
    if result != -1: 
        print ("Element is present at index % d" % result) 
    else: 
        print ("Element is not present in array")

if __name__=='__main__':
    main()
