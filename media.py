class Video():
    """
    This the video class which has the usual attributes of a title and trailer_youtube_id of the video.
    """

    def __init__(self, title, trailer_youtube_url):
        """
        Args:
            title (str): Title of the movie
            trailer_youtube_url (str): Video url for the trailer of the movie
        """

        self.title = title
        self.trailer_youtube_url = trailer_youtube_url


class Movie(Video):
    """
    This is the class of the movies whose instances could be created for replicating different movies which inherits
    the Video class.
    """

    def __init__(self, title, trailer_youtube_url, poster_image_url):
        """
        Args:
            title (str): Title of the movie
            poster_image_url (str): Url of the poster of the movie
            trailer_youtube_url (str): Video url for the trailer of the movie
        """
        Video.__init__(self, title=title, trailer_youtube_url=trailer_youtube_url)
        self.poster_image_url = poster_image_url
