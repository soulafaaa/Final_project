class file_editor():
    """ this class will hold all helper methods we will need in order to extract data from 
    the cvs file.
    
    Attributes: 
    result (String) = has he combined list of all teh responses
    
    """
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
    import pprint

    result = ""
    def response():
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        path = "/Users/soulafah/Desktop/INSY326/Final_project/client_secret.json"
        my_file = path
        creds = ServiceAccountCredentials.from_json_keyfile_name(my_file, scope)
        client = gspread.authorize(creds)

        sheet = client.open('Favorite Music Survey (Responses)').sheet1
        pp = pprint.PrettyPrinter()
        #by changing this here we get retrieve different information from the google sheet thagt is attached to out google form.
        result = sheet.get_all_values()  
        return result
        
        
        
        
    def artist(result):
        """ this method will extract all the artist and genres from the cvs file and return 
        them in a list from
        
        Args: 
            None 
        
        Returns:
            returns a list of artist and the genres associated with them. 
        
        """
    
    def songs(result):
        """ This method will extract the songs and .......... from the cvs file
        
        Return: 
            Reurns a list of all songs and their details.  
        """
        
        
ans = file_editor.response()
