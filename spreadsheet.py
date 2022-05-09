import gspread

from oauth2client.service_account import ServiceAccountCredentials
import pprint
import re

def spreadsheetReader():     
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open('Favorite Music Survey (Responses)').sheet1
    return sheet



def recommend_artist(genre):
    sheet = spreadsheetReader()

    looking_for = regexHelper(genre) 
    
    criteria_re = re.compile(looking_for)
    cells = sheet.findall(criteria_re)
    artist_name = []
    
    for cell in cells:
        if cell.col == 2: 
            artist_name.append(sheet.cell(cell.row, 3).value)
        else:
            artist_name.append(sheet.cell(cell.row, cell.col -1).value)
    
    return artist_name




def recommend_song(genre):
    #return list with tuple value 
    sheet = spreadsheetReader()
    
    # concatinating the regex value we will be loking for from the spreadsheet 
    looking_for = regexHelper(genre)
   
    criteria_re = re.compile(looking_for)
    cells = sheet.findall(criteria_re)
    song_names = []
    #looping through the cells to find the songs matchnig the genre 
    for cell in cells:
        if cell.col == 6 or cell.col == 9 or cell.col == 12: 
            song_names.append((sheet.cell(cell.row, cell.col - 2).value, sheet.cell(cell.row, cell.col - 1).value))
    
    return song_names


def regexHelper(ls): 
    looking_for = '(?i)'
    num = len(ls) -1
    for word in ls: 
        looking_for += "(?=.*\\b"+word.strip()+")"
        if ls.index(word) == num:
            looking_for += ".*$" 
            
    return looking_for
    
    

sheet = spreadsheetReader()
print(sheet.col_count)