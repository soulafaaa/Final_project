import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

     
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
client = gspread.authorize(creds)

sheet = client.open('Favorite Music Survey (Responses)').sheet1
pp = pprint.PrettyPrinter()
#by changing this here we get retrieve different information from the google sheet thagt is attached to out google form.
all_result  = sheet.get_all_values()  


     
def artist():
    """ this method will extract all the artist and genres from the cvs file and return 
        them in a list from
        
        Args: 
            None 
        
        Returns:
            returns a list of artist and the genres associated with them. 
        
        """
    # something like this .... i dont have the tiem to work on this today. can someone finsh this lease
    ans = sheet.col_values(4)
    return ans
    
    
    
    
       
    
def songs(result):
        """ This method will extract the songs and .......... from the cvs file
        
        Return: 
            Reurns a list of all songs and their details.  
        """
        


lol = artist()
print(lol)


        
    
    
