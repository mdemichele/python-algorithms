# BFS Traversal 
The basic difference in the implementation of BFS versus DFS deals with the data structure used. BFS uses a Queue data structure (which is FIFO). DFS uses a stack data structure (which is LIFO).

# BFS Pseudocode 

```
BFS (G, s)            # Where G is the graph and s is the source node  
  let Q be a queue 
  Q.enqueue( s )      # Insert s in queue to start the process. 
  
  mark s as visited 
  
  while ( Q is not empty )
    v = Q.dequeue()   # Remove the first entered vertex from queue
    
    # Process all the neighbors of V
    for all neighbors w of v in Graph G
      
      if w is not visited 
        Q.enqueue( w ) # Insert w in Q to process it in the correct order 
        mark w as visited 
```
    
  