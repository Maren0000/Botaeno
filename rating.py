import json


class Rating:
    name: str = None
    level: str = None
    chart_constant: float = 0.0
    score: int = 0
    rating: float = 0

    def __init__(self, songname: str, diff: str, constant: float, score: int):
        self.name = songname
        self.level = diff
        self.chart_constant = constant
        self.score = score

    def __str__(self):
        # return "%.1f" % self.rating
        return "%s\t%s\t%.1f\t%i\t%.3f" % (self.name, self.level, self.chart_constant, self.score, self.rating)

    def __lt__(self, other):
        return self.rating < other.rating

    def __gt__(self, other):
        return self.rating > other.rating

    def __eq__(self, other):
        return self.rating == other.rating

    def calculate_rating(self):
        boundary = [1010000, 1008000, 1004000, 1000000, 980000, 950000, 900000, 500000]
        if self.score >= boundary[0]:  # 1010000
            self.rating = self.chart_constant + 3.6
            self.rating = round(self.rating,3)

        elif self.score >= boundary[1]:
            self.rating = self.chart_constant + 3.4 + (self.score - boundary[1]) / 10000
            self.rating = round(self.rating,3)

        elif self.score >= boundary[2]:
            self.rating = self.chart_constant + 2.4 + (self.score - boundary[2]) / 4000
            self.rating = round(self.rating,3)

        elif self.score >= boundary[3]:
            self.rating = self.chart_constant + 2.0 + (self.score - boundary[3]) / 10000
            self.rating = round(self.rating,3)

        elif self.score >= boundary[4]:
            self.rating = self.chart_constant + 1.0 + (self.score - boundary[4]) / 20000
            self.rating = round(self.rating,3)

        elif self.score >= boundary[5]:
            self.rating = self.chart_constant + 0.0 + (self.score - boundary[5]) / 30000
            self.rating = round(self.rating,3)

        elif self.score >= boundary[6]:
            self.rating = self.chart_constant - 1.0 + (self.score - boundary[6]) / 50000
            self.rating = round(self.rating,3)

        elif self.score >= boundary[7]:
            self.rating = self.chart_constant - 5.0 + (self.score - boundary[7]) / 100000
            self.rating = round(self.rating,3)

        else:
            self.rating = 0

def generate_sorted_ratings(songrecords) -> list:
    ratings = []
    for songname, scores in songrecords.items():
        for diff, score in scores.items():
            if score != 0:
                rating = Rating(songname, diff, get_constant(songname, diff), scores[diff])
                rating.calculate_rating()
                ratings.append(rating)
    sorted_ratings = sorted(ratings, reverse=True)
    #for i in sorted_ratings:
    #    print(i)
    return sorted_ratings

def get_constant(songname, diff) -> int:
    with open("songinfo.json", encoding='utf-8') as jsondata:
        data = json.load(jsondata)
        for song in data["songs"]:
            if song["id"] == songname:
                for diffdata in song["difficulties"]:
                    if diffdata["ratingClass"] == diff:
                        return diffdata["ratingReal"]
                    
def CalculateRating(song, diff, score):
    return song