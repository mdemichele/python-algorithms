import sys

def make_change_helper(coins, amount, memo):
    
    print("------ Iteration ------")
    print("amount: {}".format(amount))
    
    # ---------------- BASE CASES ------------------- #
    # BASE CASE 1: If the current amount is less than 0, you've gone too far. This branch on the recursion tree is not a viable solution, so don't count it 
    if amount < 0:
        return -1
        
    # BASE CASE 2: If the current amount equals 0, you've reached a viable solution. Return a zero.
    if amount == 0:
        return 0
    
    # BASE CASE 3: You reached the current amount, so it should already be in the cache. 
    if memo[amount] != 0:
        return memo[amount]
        
        
    # Set a bogus minimum value that you'll use to compare the new minimum 
    minimum = sys.maxsize
    
    
    # ---------------- RECURSIVE CASE ------------------ #
    # RECURSIVE CASE: Call the helper function for each coin in coins 
    for coin in coins:
        # Call the helper function
        result = make_change_helper(coins, amount - coin, memo) 
        
        # Each time you call the helper function, check the returned result.
        # If result is greater than zero but less than your fake min value, set the minimum to the result 
        if result >= 0 and result < minimum:
            minimum = 1 + result 
        
        # if no miminum change number is found
        if minimum == sys.maxsize:
            memo[amount] = -1
        else:
            memo[amount] = minimum 
    
    print("memo: {}".format(memo))
    # Return the cache 
    return memo[amount]

def make_change(coins, amount):
    """Takes coins array and amount and returns the minimum number of coins to reach the amount"""
    
    # EDGE CASE 1: If amount is less than 1, there should be no solutions 
    if amount < 1:
        return 0
        
    # Create our memoization cache (array of 0s)
    memo = [0] * (amount + 1)
    
    # Call our recursive helper function 
    return make_change_helper(coins, amount, memo)
    

# Testing 
if __name__ == "__main__":
    print("Testing Make Change")
    
    print("------- TEST 1 --------")
    coins1 = [1, 2, 5]
    amount = 11
    print("make_change function started...\n")
    print("\n")
    answer = make_change(coins1, amount)
    print("make_change function ended...\n")
    print("\n")
    print("Answer should be 3: answer was {}".format(answer))