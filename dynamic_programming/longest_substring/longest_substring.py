# Problem: DNA sequence is made of characters A,C,G, and T, which represent nucleotides. A sample DNA string can be given as ACCGTTTAAAG. Finding similarities between two DNA sequences is a critical computation problem that is solved in bioinformatics. Given two DNA strings find the length of the longest common string alignment between them (it need not be continuous). Assume empty string does not match with anything.
def topdown_helper(dna1, dna2, i, j, cache):
    
    # Base Case: You've reached the beginning of each string 
    if i == 0 or j == 0:
        return 0
        
    # Recursive Case 1: if the current character in dna2 matches the current character in dna1  
    if dna1[i - 1] == dna2[j - 1]:
        cache[i][j] = 1 + topdown_helper(dna1, dna2, i - 1, j - 1, cache)
        return cache[i][j]
    else:
        cache[i][j] = max(topdown_helper(dna1, dna2, i, j - 1, cache), topdown_helper(dna1, dna2, i - 1, j, cache))
        return cache[i][j]
        
        
    
# Top-Down Function
def dna_match_topdown(dna1, dna2):
    """Should return the length of the longest continuous DNA string"""

    # Create 2-D table to store the LCS at each index 
    cache = [[0 for x in range(len(dna1) + 1)] for x in range(len(dna2) + 1)]
    
    return topdown_helper(dna1, dna2, len(dna1), len(dna2), cache)
    
    
def dna_match_bottomup(dna1, dna2):
    """Should return the length of the longest continuous DNA string"""
    
    # Create 2-D table to store the LCS at each index 
    cache = [[0 for x in range(len(dna1) + 1)] for x in range(len(dna2) + 1)]
    
    # Loop through cache and fill in values using the bottom up recurrence relation 
    for i in range(len(dna1) + 1):
        for j in range(len(dna2) + 1):
            if i == 0 or j == 0:
                cache[i][j] = 0
                
            elif dna1[i - 1] == dna2[j - 1]:
                cache[i][j] = cache[i - 1][j - 1] + 1
            
            else:
                cache[i][j] = max(cache[i - 1][j], cache[i][j - 1])
        
    # Return the value at the bottom-right index of the cache: This should be the LCS for the entire solution        
    return cache[len(dna1)][len(dna2)]


# Testing 
if __name__ == "__main__":
    
    print("\n")
    print("Testing DNAMatch")
    print("\n")
    
    # TEST 1 ##################################################################
    print("-------- Test 1 ---------")
    print("TOP-DOWN APPROACH:")
    dna1 = "A"
    dna2 = "A"
    answer = dna_match_topdown(dna1, dna2)
    print("dna1 was {}".format(dna1))
    print("dna2 was {}".format(dna2))
    print("Answer should be 1: Answer was {}".format(answer))
    
    print("\n")
    print("BOTTOM-UP APPROACH:")
    dna1 = "A"
    dna2 = "A"
    answer = dna_match_bottomup(dna1, dna2)
    print("dna1 was {}".format(dna1))
    print("dna2 was {}".format(dna2))
    print("Answer should be 1: Answer was {}".format(answer))
    
    print("\n")
    
    
    # TEST 2 ##################################################################
    print("-------- Test 2 ---------")
    print("TOP-DOWN APPROACH:")
    dna1 = "GAT"
    dna2 = "ATG"
    answer = dna_match_topdown(dna1, dna2)
    print("dna1 was {}".format(dna1))
    print("dna2 was {}".format(dna2))
    print("Answer should be 2: Answer was {}".format(answer))
    
    print("\n")
    print("BOTTOM-UP APPROACH:")
    dna1 = "GAT"
    dna2 = "ATG"
    answer = dna_match_bottomup(dna1, dna2)
    print("dna1 was {}".format(dna1))
    print("dna2 was {}".format(dna2))
    print("Answer should be 2: Answer was {}".format(answer))
    
    print("\n")
    
    
    # TEST 3 ##################################################################    
    print("-------- Test 3 ---------")
    dna1 = "ATAGTTCCGTCAAA"
    dna2 = "GTGTTCCCGTCAAA"
    answer = dna_match_topdown(dna1, dna2)
    print("dna1 was {}".format(dna1))
    print("dna2 was {}".format(dna2))
    print("Answer Should be 12: Answer was {}".format(answer))
    
    print("\n")
    print("BOTTOM-UP APPROACH:")
    dna1 = "ATAGTTCCGTCAAA"
    dna2 = "GTGTTCCCGTCAAA"
    answer = dna_match_bottomup(dna1, dna2)
    print("dna1 was {}".format(dna1))
    print("dna2 was {}".format(dna2))
    print("Answer should be 12: Answer was {}".format(answer))
    
    print("\n")