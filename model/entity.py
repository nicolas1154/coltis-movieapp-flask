class Movie:
    def __init__(self, code, name, image_url = None, year = None) -> None:
        self.code = code
        self.name = name
        self.image_url = image_url
        self.year = year
        
class Review:
    def __init__(self, name, imail, descripcion, rating, movie_code, id= None) -> None:
        self.id = id
        self.name = name
        self.imail = imail
        self.descripcion = descripcion
        self.rating = rating
        self.movie_code = movie_code

    