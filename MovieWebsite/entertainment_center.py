import fresh_tomatoes
import media
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.storyline)
avatar = media.Movie("Avatar",
                     "A marine on an alian planet",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
IronMan = media.Movie("Iron Man",
                      "Marvel Studio one of the best Movies",
                      "https://images-na.ssl-images-amazon.com/images/I/515wjJQt2nL._SY445_.jpg",
                      "https://www.youtube.com/watch?v=8hYlB38asDY")
GodFather = media.Movie("GodFather",
                        " A fictional story of new work leaders crime family",
                        "https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg",
                        "https://www.youtube.com/watch?v=i96VS_z8y7g")
mid_night_in_paris = media.Movie("Mid Night In Paris",
                                 " A fanstasy comedy film ",
                                 "https://images-na.ssl-images-amazon.com/images/I/61-nVJ7VKxL._SY355_.jpg",
                                 "https://www.youtube.com/watch?v=FAfR8omt-CY")
Love_Actually = media.Movie("Love Actually",
                            "A Romantic Movie ",
                            "https://images-na.ssl-images-amazon.com/images/I/8173d1P7CPL._SX355_.jpg",
                            "https://www.youtube.com/watch?v=fOS-HMiVejo")

movies = [toy_story,avatar,IronMan,GodFather,mid_night_in_paris,Love_Actually]
fresh_tomatoes.open_movies_page(movies)
