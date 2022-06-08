# Dijkstra's Algorithm

# Pseudocode 

```
function dijkstra(G, source)    
  
  create vertex set Q
  
  for each vertex v in Graph.Vertices:
    dist[v] <- INFINITY
    prev[v] <- UNDEFINED 
    add v to Q 
  dist[source] <- 0
  
  while Q is not empty:
    u <- vertex in Q with min dist[u]
    
    remove u from Q
    
    for each neighbor v of u still in Q:
      alt <- dist[u] + Graph.Edges(u, v)
      if alt < dist[v]:
        dist[v] <- alt 
        prev[v] <- u
        
  return dist[], prev[]
```

Using a priority Queue 

```
def Dijkstra(G, s):
  # Add nodes to min-priority queue Q with initial distance infinity 
  for v in V:
    Enqueue(Q, v, 'infinity')
    
    
  # in Q make source priority = 0
  DecreaseKey(Q, source, 0)
  
  visited = []
  #while length of Queue is valid
  while (length(Q) > 0):
    currentNode = Dequeue(Q)  # pick and delete the min distance node 
    
    visited.append(currentNode)
    
    for v in currentNode.neighbors:
      dist_V = min{dist_V, weight(currentNode, v) + dist_currentNode}
      
      DecreaseKey(Q, v, dist_V)
  ```
  
  