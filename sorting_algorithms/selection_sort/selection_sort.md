## Steps for Selection Sort 
Assuming the input is an unordered array of integers: 
1. Start with the first element in the array as the key.
2. Move from the right of the key to the end of the array, searching for the smallest element.
3. Swap smallest element with the key element. 
4. Move key one to the right and repeat steps 2-3.
5. Once the key reaches the end of the array, you are done.

## Pseudocode 
```
Function selectionSort(array):
  For i = 0 TO end of array 
    smallest = i 
    For index = i + 1 TO end of array 
      if array item index < array item smallest 
        smallest = index 
      endif 
    Next
      swap array items at index and smallest 
```

## Concept of Selection Sort
Selection sort is an in-place comparison sorting algorithm, meaning it does not use any auxiliary data structures. The only extra storage space required is for the auxiliary variable used in the swapping procedure. 

Essentially, the algorithm divides the given input array into two parts. On the left side is a sorted sublist of items from A[0]...A[key - 1]. On the right side is an unsorted sublist of items from A[key]...A[A.length - 1]. The key represents the first item in the unsorted sublist. 

The algorithm works by searching through the entire unsorted sublist from A[key + 1] -> A[A.length - 1], keeping track of the smallest element in the sublist. Upon reaching the end of the sublist, the algorithm then swaps the smallest element with the element stored at the key. Now that the element at the key is known to be smaller than the rest of the sublist, it can be considered part of the sorted sublist. We can then move the key one to the right and begin the procedure over agin. 

## Time Complexity
Selection sort has a time complexity of O(n^2). 