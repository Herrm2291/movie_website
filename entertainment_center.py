import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

school_of_rock = media.Movie("School of Rock",
                             "Struggling rock singer disguises as a substitute teacher at a prep school",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

men_in_black = media.Movie("Men in Black",
                             "2 MIB agents try to save the world from aliens",
                             "https://upload.wikimedia.org/wikipedia/en/f/fb/Men_in_Black_Poster.jpg",
                             "https://www.youtube.com/watch?v=HYUd7AOw_lk")

the_little_mermaid = media.Movie("The Little Mermaid",
                             "A mermaid wants to be human",
                             "https://upload.wikimedia.org/wikipedia/en/7/75/Movie_poster_the_little_mermaid.jpg",
                             "https://www.youtube.com/watch?v=ZGZX5-PAwR8")

pulp_fiction = media.Movie("Pulp Fiction",
                             "2 hitmen try to recover a briefcase for their boss",
                             "https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg",
                             "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

movies = [toy_story, avatar, school_of_rock, men_in_black, the_little_mermaid, pulp_fiction]

#fresh_tomatoes.open_movies_page(movies)

print(media.Movie.__doc__)
