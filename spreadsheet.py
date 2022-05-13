""" This scrit holds three functions  that are needed to extract data from  the googl sheet."""

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import re

def spreadsheetReader():     
    """ 
    This fucntion uses google drive  API to connncect our script to our google sheet.
        It returns a sheet with all the data we collected from out google form.
    
    Returns: 
        Sheet (Spreadsheet): Holds  all the data we collected from the google form 
    
    """
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open('Favorite Music Survey (Responses)').sheet1
    return sheet



def find_artist(genre):
    """ 
    This function calls the spreadsheetReader to retrun a sheet and finds all the artist names 
        we recommned
        
    Argument: 
         genre (list): value representing the user's favorite music type

    Returns: 
        artist_name (list): names of all teh artist we recommened
    """
    #return list with tuple value
    sheet = spreadsheetReader()
    
    #concatenating the regex value we will be looking for from the spreadsheet
    looking_for = regex_helper(genre) 
    criteria_re = re.compile(looking_for)
    cells = sheet.findall(criteria_re)
    artist_name = []
    
    #looping through the cells to find the artist matchnig the genre 
    for cell in cells:
        if cell.col == 2: 
            artist_name.append(sheet.cell(cell.row, 3).value)
        else:
            artist_name.append(sheet.cell(cell.row, cell.col -1).value)
    
    return artist_name


def find_song(genre):
    """ 
    This function calls the spreadsheetReader to returns a sheet and finds all the songs names 
        and the artist who sand it
        
    Argument: 
         genre (list): value representing the user's favorite music type

    Returns: 
        artist_name (list): this list contains values that are tuples. These values are the song
            name  and the artist who sings the song. 
    """
    #return list with tuple value 
    sheet = spreadsheetReader()
    
    #concatenating the regex value we will be looking for from the spreadsheet
   
    looking_for = regex_helper(genre)
    criteria_re = re.compile(looking_for)
    cells = sheet.findall(criteria_re)
    song_names = []
    
    #looping through the cells to find the songs matchnig the genre 
    for cell in cells:
        if cell.col == 6 or cell.col == 9 or cell.col == 12: 
            song_names.append((sheet.cell(cell.row, cell.col - 2).value, sheet.cell(cell.row, cell.col - 1).value))
    
    return song_names


def regex_helper(ls): 
    
    """ This is a helper method that concatenate the needed regex for the other functions to work
    
    Args:
        ls(list): represents the genre the user has inputed  
        
    Return: 
        looking_for (String): A value represnting the search for value in Regex

    """
    looking_for = '(?i)'
    num = len(ls) -1
    for word in ls: 
        looking_for += "(?=.*\\b"+word.strip()+"\\b"+")"
        if ls.index(word) == num:
            looking_for += ".*$" 
            
    return looking_for

