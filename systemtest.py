import unittest
import spreadsheet
import reccmenderSystem

class TestSpreadsheet(unittest.TestCase):
    """ 
        This class  will hold all the unit test needed to test the methods and functions
        present in spreadsheet angteh the reccmenderSystem script
    """
    
    def test_regex_helper(self):
        """ Pass in values to test regex_helper fucntion in spreadsheet  """
        
        expected_result= "(?i)(?=.*\\bcar\\b).*$"
        actual = spreadsheet.regex_helper(["car"])
        self.assertEqual(str(actual), expected_result)
        
    def test_recommend_song(self):
        """ Pass in values to test recommend_song fucntion in spreadsheet """
       
        actual = spreadsheet.recommend_song(["car"])
        expected_result= []
       
        self.assertEqual(actual, expected_result)
       
        
    def test_recommend_song_2(self):
        """ Pass in values to test recommend_song fucntion in spreadsheet """
        
        acutal = spreadsheet.recommend_song(["Pop","Country"])
        expected_result= [('All Too Well - 10 minute version', 'Taylor Swift')]
       
        self.assertListEqual(acutal, expected_result)
        
        
    def test_recommend_artist_1(self):
        """ Pass in values to test recommend_artist fucntion in spreadsheet """
       
        acutal = spreadsheet.recommend_artist(["Pop","Country"])
        expected_result= [ 'Taylor Swift']
        self.assertListEqual(acutal, expected_result)
   
   
    def test_recommend_artist_2(self):
        """ pass in values to test recommend_artist fucntion in spreadsheet """
       
        acutal = spreadsheet.recommend_artist(["EDM"])
        expected_result = ['Adventure club']
        self.assertListEqual(acutal, expected_result)
        
        
        
        
        
    

        
        
        
	
 






maybe = unittest.TestLoader() \
                       .loadTestsFromTestCase(TestSpreadsheet)
runner = unittest.TextTestRunner()
runner.run(maybe)