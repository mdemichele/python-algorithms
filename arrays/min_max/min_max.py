
def min_max(arr) -> ():
    """Accepts a one dimensional array and returns a Python tuple of the min and max in the form (min, max)"""
    
    min = arr[0]
    max = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < min:
            min = arr[i]
        
        if arr[i] > max:
            max = arr[i]
    
    return (min, max)

if __name__ == "__main__":
    answer = min_max([3,9,5,2,7])
    print(answer)
    