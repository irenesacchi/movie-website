import webbrowser

# The name of the Class
class Movie():
    """This class provides a way to store movie provided informations"""
    
    # The Constructor and the relative Variables
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # The Method to open the youtube url
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
