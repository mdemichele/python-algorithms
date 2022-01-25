# Unbound Knapsack Problem

One formulation of the problem goes like this:

"Suppose you woke up on a mysterious island and there are numerous valuable items on the island. You have a knapsack (a bag) with you which you can use to take back these items with you. But, the problem is there is a limit to the weight that your knapsack can carry. So, our questions would be what is the best way to cram items into our knapsack to maximize the overall value of items that you can carry back with you."

# Psuedocode 

knapsack(max_weight, n, weights[], values[]):
  
  memo = [0] * (max_weight + 1)
  
  for x in range(max_weight + 1):
    for i in range(memo):
      if weights[i] < x:
        memo[x] = max(memo[x], memo[x - weights[i]] + values[i])
  
  return memo[max_weight]