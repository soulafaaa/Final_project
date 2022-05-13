""" 
   This script hold the recommendation class that will invoke function from the 
   spreadsheet script it will also collect responses from users in teh main function
   and will pass the arguments into the recommendation class.
"""
import sys 
import re 
import spreadsheet as sp

class Recomendation():
    """ 
    This class will retrun the user reccomenation  by invoking fucntions from 
        spreadsheet script
        
    Attributes:
        genre (string): value representing the user's favorite music type, this value will 
            than be turned into a list 
    """
    
    def __init__(self, genre):
        """
        Initializes a Recomendation object.

        Args:
            genre (string): value representing the user's favorite music type,

        """
        self.genre = genre
    
    
    def artist_rec(self): 
        """ 
        This methods will call recommend_artist function from the spreadsheet
        
        Return: 
          ans (String) : A value represnting the artist suggestion  
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
        This methods will call recommend_song function from the spreadsheet
    
        Return: 
            ans: value represnting the song suggestion  with the artist name
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
                ans += song[0] + " by "+ song[1]+ ", "
            # remove the extra comma at the end 
             ans = ans[:-2]
        else:
            ans = "\n\033[31mI'm sorry please try another input!\033[0m"
    
        return ans
    

        
    
def main():
    """ 
    This function will collect user input and pass the responses into methods from the 
        recomendation class
        
    Return: 
        String value that represnts the recommended music. 
    """
    
    
    while True:
         name = input("What is your name? ")
         if checkString(name): 
            print (f"\n\033[33mHello,{name}! We offer two different kinds of recommendation.\033[0m\n" 
                     "\033[31mOption A: an artist recommendation based on your favorite genre.\n"
                     "Option B:a song recommendation based on your  favorite genre.\n\033[0m")
            rec_type = input("What kind of recomendation would you like today? Type A or B\n")
            if checkString(rec_type):
                if rec_type.strip() == "A"| rec_type.strip() == "a":
                    fav_genre = input("what is your favorite genre?"
                                      " (if more than one separate answers with space)\n")
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
                    
                if rec_type.strip() == "B" | rec_type.strip() == "b" :
                     fav_genre = input("what is your favorite genre?"
                                      "(if more than one separate answers with space)\n")
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
    A helper function that uese regex to make sure the user has inpouted an acepted value
    
    Args: 
        word (string): a string that represent the user input 
        
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
