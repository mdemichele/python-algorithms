# top-down approach 
def topdown_helper(n, cache):
    
    # Base Case 1: You go past the bottom step (i.e. NOT a solution)
    if n < 0:
        return 0
        
    # Base Case 2: You reach the bottom step (i.e. you've found a solution)
    elif n == 0:
        return 1
    
    # Base Case 3: Value is already in the cache 
    elif cache.get(n) != None:
        return cache[n]
        
    # Recursive Case: step down 1 step and step down 2 steps 
    else:
        cache[n] = topdown_helper(n - 1, cache) + topdown_helper(n - 2, cache)
        return cache[n]
    
    
def climbing_staircase(n):
    """Returns the number of ways to climb to the specified staircase"""
    cache = {}
    return topdown_helper(n, cache)

# Testing 
if __name__ == "__main__":
    
    print("Testing Climbing Staircase")
    
    # TEST 1 ###################################################################
    print("----------------------- TEST 1 -------------------------")
    print("\n")
    n = 3
    answer = climbing_staircase(n)
    print("Answer should be 3: Answer was {}".format(answer))
    
    # TEST 2 ##################################################################
    print("----------------------- TEST 2 -------------------------")
    print("\n")
    n = 10
    answer = climbing_staircase(n)
    print("Answer should be 89: Answer was {}".format(answer))