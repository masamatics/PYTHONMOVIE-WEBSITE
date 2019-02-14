
#This is the main python code to store info for movies.

import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A Story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

social_network = media.Movie("The Social Network",
                             "A story of how facebook was founded",
                             "https://upload.wikimedia.org/wikipedia/en/7/7a/Social_network_film_poster.jpg",
                             "https://www.youtube.com/watch?v=lB95KLmpLR4")

intersteller = media.Movie("Intersteller",
                           "A story about saving earth and love can transcend through time and space",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=Lm8p5rlrSkY")

martian = media.Movie("The Martian",
                      "A story about a man left on mars",
                      "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",
                      "https://www.youtube.com/watch?v=ej3ioOneTy8")

guilt_trip = media.Movie("The Guilt Trip",
                         "A story abotu a son and a mother decided to go on a road trip",
                         "https://upload.wikimedia.org/wikipedia/en/0/0a/The_Guilt_Trip_Poster.jpg",
                         "https://www.youtube.com/watch?v=7FMQLzOq1i4")

movies = [toy_story, avatar, social_network, intersteller, martian, guilt_trip]
fresh_tomatoes.open_movies_page(movies)






