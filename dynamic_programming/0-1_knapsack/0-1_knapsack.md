# 0-1 Knapsack Problem 

The 0-1 knapsack problem is formulated the same way as the unbound knapsack problem, expect for the fact that you can only use each item in the knapsack a maximum of once. Here's a formulation of the problem:

"Suppose you woke up on a mysterious island and there are numerous valuable items on the island. You have a knapsack (a bag) with you which you can use to take back these items with you. But, the problem is there is a limit to the weight that your knapsack can carry. So, our questions would be what is the best way to cram items into our knapsack to maximize the overall value of items that you can carry back with you."

# Pseudocode 

knapsack(max_weight, n, weights[], values[]):

  memo = [[0 for x in range(n+1)] for x in range(max_weight + 1)]
  
  for x in range(max_weight + 1):
    for i in range(n + 1):
        memo[x, i] = memo[x, i - 1]
        
        current_weight = weights[i]
        current_value = values[i]
        
        if x >= current_weight:
          memo[x, i] = max(memo[x, i], memo[x - current_weight] + current_value)
  
  return memo[x, n]