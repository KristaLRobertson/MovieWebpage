import webbrowser

#This string allows for the defined details associated with the movie to be put out or in
class Movie():    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster =  poster_image
        self.trailer_youtube_url = trailer_youtube
#this string defines the show_trailer function and allows the youtube video to play
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
