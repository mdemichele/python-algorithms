
def selectionSort(arr):
    # iterate through the entire array 
    for i in range(0, len(arr)):
        
        # Set the current index as the index of the new smallest number 
        smallest = i 
        
        # Iterate from one right of current index through the rest of the array 
        for index in range(i + 1, len(arr)):
            
            # If you come across a value that is smaller than current smallest, set smallest to new index 
            if arr[index] < arr[smallest]:
                smallest = index 
        
        # Swap the current index with the index of the new smallest 
        # NOTE: if current index was already the smallest, no swapping will take place here. 
        temp = arr[smallest]
        arr[smallest] = arr[i]
        arr[i] = temp 
    
    # Return the sorted array 
    return arr 

# Testing 
if __name__ == "__main__":
    
    print("Testing Selection Sort")
    
    print("-------- TEST 1 ----------")
    print("Unsorted Array: [9, 7, 4, 1, 6, 2]")
    arr = [9,7,4,1,6,2]
    sorted = selectionSort(arr)
    print("Sorted Array should be: [1,2,4,5,7,9]: Sorted Array was {}".format(sorted))
    