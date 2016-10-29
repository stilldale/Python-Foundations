import fresh_tomatoes
import media

#This module creates new instances of the Movie class from the media module for each of my favorite movies.
#Movie objects are created by passing the following parameters: Name, Description, Poster URL, and Trailer URL.

inception = media.Movie("Inception",
                        "A movie about entering different states of consciousness to explore belief systems",
                        "http://www.impawards.com/2010/posters/inception.jpg",
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")

interstellar = media.Movie("Interstellar",
                        "A movie about human responsability to challenge our understanding of reality in the service of others",
                        "https://s-media-cache-ak0.pinimg.com/originals/a6/f7/03/a6f703744d5d2c1e5a5a110272c97b2f.jpg",
                        "https://www.youtube.com/watch?v=2LqzF5WauAw")

matrix1 = media.Movie("The Matrix",
                     "Part 1 of the greatest story ever told about the nature of reality and the struggle for different forms of consciousness to exist",
                     "http://thebitplayers.net/wp-content/uploads/2015/08/the-matrix-movie-poster.jpg",
                     "https://www.youtube.com/watch?v=Q8g9zL-JL8E")

matrix2 = media.Movie("The Matrix Reloaded",
                     "Part 2 of the greatest story ever told about the nature of reality and the struggle for different forms of consciousness to exist",
                     "https://s-media-cache-ak0.pinimg.com/originals/f6/1a/cb/f61acbcf19983d06a81a1ad103e35485.jpg",
                     "https://www.youtube.com/watch?v=kYzz0FSgpSU")

matrix3 = media.Movie("The Matrix Revolutions",
                     "Part 3 of the greatest story ever told about the nature of reality and the struggle for different forms of consciousness to exist",
                     "http://www.impawards.com/2003/posters/matrix_revolutions.jpg",
                     "https://www.youtube.com/watch?v=hMbexEPAOQI")

terminator2 = media.Movie("Terminator 2: Judgment Day",
                     "Also a dope movie about the events leading to the AI revolution",
                     "http://blog.signalnoise.com/wp-content/uploads/2012/08/i_t2.jpg",
                     "https://www.youtube.com/watch?v=7QXDPzx71jQ")

movies = [inception, interstellar, terminator2, matrix1, matrix2, matrix3]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)


print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
