import os, json
import math

import rating

class Profile:
    ShortID: str = None
    Rating: float = 0.0
    Exp: int = 0
    Level: int = 0
    DisplayName: str = None
    Badge: str = None
    Character: str = None
    Background: str = None
    I_Stats: list = []
    I_Clear = int = 0
    I_FC = int = 0
    I_AP = int = 0
    I_APP = int = 0 #Not in friend data API yet
    II_Stats: list = []
    II_Clear = int = 0
    II_FC = int = 0
    II_AP = int = 0
    II_APP = int = 0 #Not in friend data API yet
    III_Stats: list = []
    III_Clear = int = 0
    III_FC = int = 0
    III_AP = int = 0
    III_APP = int = 0 #Not in friend data API yet
    IV_Stats: list = []
    IV_Clear = int = 0
    IV_FC = int = 0
    IV_AP = int = 0
    IV_APP = int = 0 #Not in friend data API yet
    IV_A_Stats: list = []
    IV_A_Clear = int = 0 #Not in friend data API yet
    IV_A_FC = int = 0 #Not in friend data API yet
    IV_A_AP = int = 0 #Not in friend data API yet
    IV_A_APP = int = 0 #Not in friend data API yet
    Ratings: list

    def ParseProfile(self, jsondata):
        self.ShortID = jsondata["shortId"]
        self.Rating = jsondata["rating"]
        self.Exp = jsondata["exp"]
        self.calcLevel()
        self.DisplayName = jsondata["displayName"]
        self.Badge = jsondata["badgeId"]
        self.Character = jsondata["characterId"]
        self.Background = jsondata["backgroundId"]
        self.I_Stats = [jsondata["playStats"]["i"]["clearCount"], jsondata["playStats"]["i"]["fcCount"], jsondata["playStats"]["i"]["apCount"]]
        self.II_Stats = [jsondata["playStats"]["ii"]["clearCount"], jsondata["playStats"]["ii"]["fcCount"], jsondata["playStats"]["ii"]["apCount"]]
        self.III_Stats = [jsondata["playStats"]["iii"]["clearCount"], jsondata["playStats"]["iii"]["fcCount"], jsondata["playStats"]["iii"]["apCount"]]
        self.IV_Stats = [jsondata["playStats"]["iv"]["clearCount"], jsondata["playStats"]["iv"]["fcCount"], jsondata["playStats"]["iv"]["apCount"]]
        self.Ratings = rating.generate_sorted_ratings(jsondata["scores"])
        return self

    
    def calcLevel(self):
        #math to calc level from exp
        pass


def ReadUserProfile(string):
    userProfile = Profile()
    filename = "users/" + string + ".json"
    with open(filename, "r") as jsondata:
        data = json.load(jsondata)
        '''ShortID = data["shortId"]
        Rating = data["rating"]
        Level = data["exp"]
        Name = data["displayName"]
        IClear = data["playStats"]["i"]["clearCount"]
        IFC = data["playStats"]["i"]["fcCount"]
        IAP = data["playStats"]["i"]["apCount"]
        IIClear = data["playStats"]["ii"]["clearCount"]
        IIFC = data["playStats"]["ii"]["fcCount"]
        IIAP = data["playStats"]["ii"]["apCount"]
        IIIClear = data["playStats"]["iii"]["clearCount"]
        IIIFC = data["playStats"]["iii"]["fcCount"]
        IIIAP = data["playStats"]["iii"]["apCount"]
        IVClear = data["playStats"]["iv"]["clearCount"]
        IVFC = data["playStats"]["iv"]["fcCount"]
        IVAP = data["playStats"]["iv"]["apCount"]
        Badge = data["badgeId"]
        Character = data["characterId"]
        Background = data["backgroundId"]
        ratings = rating.generate_sorted_ratings(data["scores"])'''
        userProfile.ParseProfile(data)
        

    #This could be simiplified a bunch
    ratfloat = math.floor(float(userProfile.Rating))
    match ratfloat:
        case 0 | 1:
            RatingColor = "134, 255, 2"
            RatingIcon = "Rating Tier 1"
        case 2 | 3:
            RatingColor = "6, 255, 2"
            RatingIcon = "Rating Tier 2"
        case 4 | 5 | 6:
            RatingColor = "9, 255, 104"
            RatingIcon = "Rating Tier 3"
        case 7:
            RatingColor = "2, 224, 255"
            RatingIcon = "Rating Tier 4"
        case 8:
            RatingColor = "2, 224, 255"
            RatingIcon = "Rating Tier 5"
        case 9:
            RatingColor = "2, 224, 255"
            RatingIcon = "Rating Tier 6"
        case 10:
            RatingColor = "252, 217, 6"
            RatingIcon = "Rating Tier 7"
        case 11:
            RatingColor = "252, 217, 6"
            RatingIcon = "Rating Tier 8"
        case 12:
            RatingColor = "255, 9, 11"
            RatingIcon = "Rating Tier 9"
        case 13:
            RatingColor = "252, 15, 174"
            RatingIcon = "Rating Tier 10"
        case 14:
            RatingColor = "217, 13, 255"
            RatingIcon = "Rating Tier 11"
        case 15:
            RatingColor = "252, 131, 1"
            RatingIcon = "Rating Tier 12"
        case 16:
            RatingColor = "252, 129, 1"
            RatingIcon = "Rating Tier 13"
        

    return userProfile, RatingColor, RatingIcon

        
