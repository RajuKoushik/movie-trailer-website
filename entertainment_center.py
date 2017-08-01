import fresh_tomatoes
import media


def personalised_movies_list():
    """This fucltion returns the list of personaled movies list"""

    deadpool = media.Movie(title='Deadpool', trailer_youtube_url='https://www.youtube.com/watch?v=gtTfd6tISfw',
                           poster_image_url='https://s-media-cache-ak0.pinimg.com/originals/00/e5/93/00e593607694b56314a6e9bd6095986d.jpg')  # noqa

    pursuit_of_happiness = media.Movie(title='Pursuit of Happiness',
                                       trailer_youtube_url='https://www.youtube.com/watch?v=89Kq8SDyvfg',  # noqa
                                       poster_image_url='https://s-media-cache-ak0.pinimg.com/736x/91/94/bb/9194bbfac3481c4940c6c0c2afdbe16b--pursuit-of-happiness-the-pursuit-of-happyness.jpg')  # noqa

    inception = media.Movie(title='Inception', trailer_youtube_url='https://www.youtube.com/watch?v=8hP9D6kZseM',
                            poster_image_url='https://s.aolcdn.com/dims5/amp:33d46f2e8d0d23c2a537408cab362e84d00af849/r:360,540/q:70/?url=http%3A%2F%2Faolx.tmsimg.com%2Fmovieposters%2Fv8%2FAllPhotos%2F7825626%2Fp7825626_p_v8_af.jpg%3Fw%3D360')  # noqa

    batman = media.Movie(title='Batman', trailer_youtube_url='https://www.youtube.com/watch?v=1T__uN5xmC0',
                         poster_image_url='http://www.impulsegamer.com/articles/wp-content/uploads/2015/04/3001312_press01.jpg')  # noqa

    wolf_of_wallstreet = media.Movie(title='Wolf of Wallstreet',
                                     trailer_youtube_url='https://www.youtube.com/watch?v=iszwuX1AK6A',  # noqa
                                     poster_image_url='https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxMjgxNTk0MF5BMl5BanBnXkFtZTgwNjIyOTg2MDE@._V1_UY1200_CR90,0,630,1200_AL_.jpg')  # noqa

    movie_list = [deadpool, pursuit_of_happiness, inception, batman, wolf_of_wallstreet]

    return movie_list


fresh_tomatoes.open_movies_page(personalised_movies_list())
