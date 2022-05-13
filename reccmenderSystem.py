""" 
   This script holds the recommendation class that will invoke functions from the 
   spreadsheet script. Additionally, it will collect responses from users in the main function
   and pass the arguments into the recommendation class.
"""
import sys 
import re 
import spreadsheet as sp

class Recomendation():
    """ 
    This class will retrun the user recommendation by invoking fucntions from 
        spreadsheet script.
        
    Attributes:
        genre (string): value representing the users' favorite music type; this value will 
            then be turned into a list 
    """
    
    def __init__(self, genre):
        """
        Initializes a Recommendation object

        Args:
            genre (string): value representing the user's favorite music type

        """
        self.genre = genre
    
    
    def artist_rec(self): 
        """ 
        These methods will call the recommend_artist function from the spreadsheet.
        
        Return: 
          ans (str) : A value represnting the artist suggestion  
        """
        #slitting the genrea into a list 
        ls = self.genre.split()
        genre_red = sp.find_artist(ls)
       
        ans = ""
        #concatinating the final recomendation 
        if genre_red: 
            ans = "\nBased on your input "
            if len(ls) > 1:
                for i in ls:
                    ans += i + ", "
            else: ans += ls[0] +" "
            ans += "your artist suggestion for today are: " 
            for artist in genre_red:
                ans += artist + ", "
            # remove the extra comma at the end 
            ans = ans[:-2]
        else:
            ans = "\n\033[31mI'm sorry please try another input!\033[0m"
    
        return ans
    
    
    def song_rec(self): 
        """ 
        This method will call the recommend_song function from the spreadsheet.
    
        Return: 
            ans: value represnting the song suggestion with the artist name
        """
        #slitting the genrea into a list 
        ls = self.genre.split()
        genre_red = sp.find_song(ls)
       
        ans = ""
        #concatinating the final recomendation 
        if genre_red: 
             ans = "\nBased on your input "
             if len(ls) > 1:
                for i in ls:
                    ans += i + ", "
             else: ans += ls[0] +" "
             ans += "your song suggestion for today are: " 
             for song in genre_red:
                ans += song[0] + "\033[33m by "+ song[1]+ "\033[0m, "
            # remove the extra comma at the end 
             ans = ans[:-2]
        else:
            ans = "\n\033[31mI'm sorry please try another input!\033[0m"
    
        return ans
    

        
    
def main():
    """ 
    This function will collect user input and pass the responses into methods from the 
        recomendation class.
        
    Return: 
        String value that represents the recommended music. 
    """
    
    
    while True:
         name = input("What is your name? ")
         if checkString(name): 
            print (f"\n\033[33mHello,{name}! We offer two different kinds of recommendation.\033[0m\n" 
                     "\033[31mOption A: an artist recommendation based on your favorite genre.\n"
                     "Option B:a song recommendation based on your  favorite genre.\n\033[0m")
            rec_type = input("What kind of recomendation would you like today? Type A or B\n")
            if checkString(rec_type):
               # incase a user inputs lower case
                look_for_1 = "A"
                look_for_1 = look_for_1.casefold()
                
                if rec_type.strip().casefold() == look_for_1:
                    fav_genre = input("What is your favorite genre?"
                                      " (If more than one separate answers with space)\n")
                    if checkString(fav_genre):
                        #creating an isntance of the recomendation class 
                        rec = Recomendation(fav_genre)
                        rec = rec.artist_rec()
                        print(rec)
                        if rec == "\n\033[31mI'm sorry please try another input!\033[0m":
                            #continuous loop if we couldn't find a recommendation
                            continue
                        else:
                            break
                        
                # incase a user inputs lower case
                look_for_2 = "B"
                look_for_2 = look_for_2.casefold()   
                if rec_type.strip().casefold() == look_for_2:
                     fav_genre = input("What is your favorite genre?"
                                      " (If more than one separate answers with space)\n")
                    #call song rec
                     if checkString(fav_genre):
                        #creating an isntance of the recomendation class 
                        rec = Recomendation(fav_genre)
                        rec = rec.song_rec()
                        print(rec)
                        if rec == "\n\033[31mI'm sorry please try another input!\033[0m":
                            #continuous loop if we couldn't find a recommendation
                            continue
                        else:
                            break
                    
                    
                
def checkString(word):
    """ 
    A helper function that uses regex to make sure the user has inputted an accepted value.
    
    Args: 
        word (string): a string that represents the user input 
        
    Return: 
        value (boolean): returns a boolean depending on whether the user has inputted an accepted value
    """
    validate = re.findall(r'[a-zA-Z]+|[&]+|[-]+', word)
    value = True 
    if not validate:
        value = False 
    return value
    
     

if __name__ =="__main__":
    main()
