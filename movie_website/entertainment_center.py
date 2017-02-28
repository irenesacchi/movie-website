import media
import fresh_tomatoes

# 6 object for the Class Movie
avatar = media.Movie("Avatar",
                     "A marine sent to Pandora will choose between following orders or protecting the place he loves",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

kingdom = media.Movie("kingdom of heaven",
                      "Balian travels to Jerusalem during the crusades to finds himself as a true knight",
                      "https://upload.wikimedia.org/wikipedia/en/9/9e/KoHposter.jpg",
                      "https://www.youtube.com/watch?v=moNH4N44D28")

inside_out = media.Movie("Inside out",
                         "It is all about emotions: Joy, Fear, Anger, Disgust and Sadness",
                         "https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg",
                         "https://www.youtube.com/watch?v=WIDYqBMFzfg&t=2s")


pirates = media.Movie("Pirates of the Caribbean",
                      "A story about pirates and about a girl who wants do become one",
                      "https://upload.wikimedia.org/wikipedia/en/0/0e/Pirates_of_the_Caribbean_movie.jpg",
                      "https://www.youtube.com/watch?v=naQr0uTrH_s")


casino_royale = media.Movie("Casino Royale",
                            "a 007 adventure",
                            "http://www.impawards.com/2006/posters/casino_royale.jpg",
                            "https://www.youtube.com/watch?v=36mnx8dBbGE")

pulp_fiction = media.Movie("Pulp fiction",
                           "complicated interraleted stories Tarantino style",
                           "https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg",
                           "https://www.youtube.com/watch?v=tGpTpVyI_OQ")

# the object list
movies = [avatar, kingdom, inside_out, pirates, casino_royale, pulp_fiction]
# inside fresh_tomato the open_movie_page will be initiated
fresh_tomatoes.open_movies_page(movies)
