# Unbound Knapsack Problem

One formulation of the problem goes like this:

"Suppose you woke up on a mysterious island and there are numerous valuable items on the island. You have a knapsack (a bag) with you which you can use to take back these items with you. But, the problem is there is a limit to the weight that your knapsack can carry. So, our question would be: what is the best way to cram items into our knapsack to maximize the overall value of items that you can carry back with you."

You can reuse the items as many times as you'd like up to the max weight. For instance, say you have an item which weighs 1 pound and is worth 10 dollars. Let's say this item is a baseball. Let's also say that the max weight is 5 pounds. 

In this scenario, you can cram up to 5 baseballs in your knapsack until you reach the max weight. This would give you a total of 50 dollars worth of items. This is great. But, the question is, is this the maximum amount of dollar value you can cram into your knapack without going over the weight limit?

# Psuedocode 

knapsack(max_weight, n, weights[], values[]):
  
  memo = [0] * (max_weight + 1)
  
  for x in range(max_weight + 1):
    for i in range(memo):
      if weights[i] < x:
        memo[x] = max(memo[x], memo[x - weights[i]] + values[i])
  
  return memo[max_weight]

# Psuedocode Explanation

In the above psuedocode, we have a function called knapsack. We feed this function with four parameters. `max_weight` is the maximum allowed weight represented as an integer. `n` is the current index. `weights[]` is an array representing the weights of the objects on the island. `values[]` is an array representing the values of the objects on the island. The indices of the weights and values array correspond to the same item. 



