import unittest
import spreadsheet
import reccmenderSystem

class TestSpreadsheet(unittest.TestCase):
    """ 
        This class  will hold all the unit test needed to test all the functions
        present in spreadsheet script. 
    """
    
    def test_regex_helper(self):
        """ Pass in values to test regex_helper fucntion in spreadsheet  """
        
        expected_result= "(?i)(?=.*\\bcar\\b).*$"
        actual = spreadsheet.regex_helper(["car"])
        self.assertEqual(str(actual), expected_result)
        
    def test_recommend_song(self):
        """ Pass in values to test recommend_song fucntion in spreadsheet """
       
        actual = spreadsheet.find_song(["car"])
        expected_result= []
        self.assertEqual(actual, expected_result)
       
        
    def test_recommend_song_2(self):
        """ Pass in values to test recommend_song fucntion in spreadsheet """
        
        acutal = spreadsheet.find_song(["Pop","Country"])
        expected_result= [('All Too Well - 10 minute version', 'Taylor Swift')]
        self.assertListEqual(acutal, expected_result)
        
        
    def test_recommend_artist_1(self):
        """ Pass in values to test recommend_artist fucntion in spreadsheet """
       
        acutal = spreadsheet.find_artist(["Pop","Country"])
        expected_result= [ 'Taylor Swift']
        self.assertListEqual(acutal, expected_result)
   
   
    def test_recommend_artist_2(self):
        """ pass in values to test recommend_artist fucntion in spreadsheet """
       
        acutal = spreadsheet.find_artist(["EDM"])
        expected_result = ['Adventure club']
        self.assertListEqual(acutal, expected_result)
        
        
    
    
        
             
        
	##change what is the load test to run test 
testSpreadsheet = unittest.TestLoader() \ .loadTestsFromTestCase(TestSpreadsheet)
runner = unittest.TextTestRunner()
runner.run(testSpreadsheet)
