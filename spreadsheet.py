import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

     
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
client = gspread.authorize(creds)

sheet = client.open('Favorite Music Survey (Responses)').sheet1
pp = pprint.PrettyPrinter()
#by changing this here we get retrieve different information from the google sheet thagt is attached to out google form.



def getartist(name):
    # we need to find all the cells that have that artist name in 
    ans = sheet.findall(name)
    print(ans)
    
    
getartist("beyonce")



