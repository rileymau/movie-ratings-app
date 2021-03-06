"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db



#add app route later, example has method=post
def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)
    # later tbd user = User(email=request.form['email]', password=request.form['password'])

    db.session.add(user)
    db.session.commit()

    return user

def get_users():
    """Return a users."""

    return User.query.all()


def get_user_by_id(user_id):
    """get each user for user webpages"""

    return User.query.get(user_id)

def get_user_by_email(email):
    """check if email is already in users.emails"""

    return User.query.filter(User.email == email).first()


def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""
    movie = Movie(title=title, overview=overview, release_date = release_date, poster_path=poster_path)

    db.session.add(movie)
    db.session.commit()

    return movie

def get_movies(): 
    """Return all movies"""

    return Movie.query.all()

def get_movie_by_id(movie_id):
    """get each move for movie webpages"""

    return Movie.query.get(movie_id)


def create_rating(user, movie, score):
    """Create and return a new rating."""
    rating = Rating(user=user, movie=movie, score=score)
    #assign user and movie variable to movie and user objects
    # #enter user and movie objects into create_rating above 

    db.session.add(rating)
    db.session.commit()

    return rating



if __name__ == '__main__':
    from server import app
    connect_to_db(app)
  
    