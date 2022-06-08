# DFS Traversal
The basic different in the implementation of DFS versus BFS deals with the data structure used. DFS uses a Stack data structure (which is LIFO). BFS uses a Queue data structure (which is FIFO).

# DFS Pseudocode 

```
DFS (G, s)                                # Where G is the graph and s is the source node 
  let S be a stack 
  S.push( s )                             # Insert s in stack to start the process
  
  while ( S is not empty )    
    v = S.pop()                           # Remove the top vertex from the stack 
    
    if v is not marked as visited then
      mark v as visited
    
      for all neighbors w of v in Graph G
        S.push ( w )                      # Insert w in S to process it in the correct order 