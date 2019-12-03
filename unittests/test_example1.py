#https://www.youtube.com/watch?v=6tNS--WetLI
import unittest
import example1 as ex

class Test_example1(unittest.TestCase): #testing capabilites
    def test_add(self):   #test_whatyouaretesting. This is important
        #result = ex.add(10,5)
        self.assertEqual(ex.add(10,5), 15)
        self.assertEqual(ex.add(10, -15), -5)

    def test_sub(self):   #test_whatyouaretesting. This is important
        #result = ex.add(10,5)
        self.assertEqual(ex.sub(10,5), 5)

    def test_divide(self):
        self.assertRaises(ValueError, ex.divide, 10, 0) #ValueError is raised for function iwht arguments
        self.assertRaises(ValueError, ex.divide, 10, 2)  # this will raise the error





if __name__ == "__main__":
    unittest.main()




'''
Method	                            Checks that
assertEqual(a,b)	                a==b
assertNotEqual(a,b)	                a != b
assertTrue(x)	                    bool(x) is True
assertFalse(x)	                    bool(x) is False
assertIs(a,b)	                    a is b
assertIs(a,b)	                    a is b
assertIsNot(a, b)	                a is not b
assertIsNone(x)	                    x is None
assertIsNotNone(x)	                x is not None
assertIn(a, b)	                    a in b
assertNotIn(a, b)	                a not in b
assertIsInstance(a, b)	            isinstance(a, b)
assertNotIsInstance(a, b)	        not isinstance(a, b)
'''

'''
to run the unittiest 
python -m unittest test_example1.py
'''