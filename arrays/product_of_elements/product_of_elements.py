# Last Updated: 30 January 2025

def product_of_elements(input) -> list:
    
    answer = []

    for i in range(0, len(input)):

        pre_product = 1
        for j in range (i - 1, -1, -1):
            pre_product = input[j] * pre_product
        
        post_product = 1
        for k in range (i + 1, len(input)):
            post_product = input[k] * post_product
        
        answer.append(pre_product * post_product)
    
    return answer

# Testing
if __name__ == "__main__":
    input = [1, 2, 3, 4, 5]

    expected = [120, 60, 40, 30, 24]

    answer = product_of_elements(input)
    print("Expected answer: ")
    print(expected)
    print("Actual answer: ")
    print(answer)