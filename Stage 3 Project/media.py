import webbrowser

class Movie():
    # This class provides a way to store movie related information

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        # initialize instance of class Movie
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    
    def show_trailer(self):
        # function to show movie trailer
        webbrowser.open(self.trailer_youtube_url)
