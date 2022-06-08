import unittest
import balanced_brackets

class TestCase(unittest.TestCase):
    
    # Test 1: Should always work for valid bracket 
    def test1(self):
        string = "()"
        expected = True 
        self.assertEqual(balanced_brackets.balanced_brackets(string), expected)
        
    # Test 2: Should fail for invalid bracket 
    def test2(self):
        string = "("
        expected = False 
        self.assertEqual(balanced_brackets.balanced_brackets(string), expected)
        
    # Test 3: Should work for valid bracket 
    def test3(self):
        string = "({[]})"
        expected = True 
        self.assertEqual(balanced_brackets.balanced_brackets(string), expected)
        
    # Test 4: Should work for invalid bracket 
    def test4(self):
        string = "({}])"
        expected = False 
        self.assertEqual(balanced_brackets.balanced_brackets(string), expected)
        
if __name__ == "__main__":
    unittest.main()