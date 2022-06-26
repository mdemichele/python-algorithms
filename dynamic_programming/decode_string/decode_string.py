
def decode_string_helper(string, count):
    """Helper function for decode_string"""

    # BASE CASE: No valid encoding can start with 0
    if string.startswith("0"):
        return 0
    
    # BASE CASE 1: String is one letter long or empty string
    if len(string) <= 1:
        return 1
    
    # RECURSIVE CASE 1: Encodes just the first encoding 
    count += decode_string_helper(string[1:], count)

    # RECURSIVE CASE 2: Encodes the two digit encoding 
    if int(string[:2]) <= 26:
        count += decode_string_helper(string[2:], count)

    return count 



# Decode String Function 
def decode_string(string):
    """returns the number of ways the entered string can be decoded"""
    answer = decode_string_helper(string, 0)
    return answer




if __name__ == "__main__":
    # TEST CASE 1: "1"
    answer = decode_string("1")
    print("TEST CASE 1: 1")
    print(answer)

    # TEST CASE 2: "111"
    answer = decode_string("111")
    print("TEST CASE 2: 111")
    print(answer)

    # TEST CASE 3: "0111"
    answer = decode_string("0111")
    print("TEST CASE 2: 0111")
    print(answer)