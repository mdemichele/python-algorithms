# Unbound Knapsack Problem 
def unbound_knapsack(max_weight, current, weights, values):
    memo = [0] * (max_weight + 1)
    
    for x in range(0, max_weight + 1):
        current = x 
        for i in range(0, current):
            if weights[i] <= x:
                memo[x] = max(memo[x], memo[x - weights[i]] + values[i])
    
    return memo[max_weight]


# Testing 
if __name__ == "__main__":
    
    print("Testing Unbound Knapsack")
    
    print("----------- Test 1 ----------------")
    max_weight = 5
    weights = [1, 2, 3, 4, 5]
    values = [10, 5, 20, 15, 9]
    answer = unbound_knapsack(max_weight, 0, weights, values)
    print("weights: [1,2,3,4,5]")
    print("values: [10,5,20,15,9]")
    print("Answer should be 50: answer was {}".format(answer))