"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
    redirect)

from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined 

@app.route('/')
def homepage():
    """View homepage."""
    return render_template('homepage.html')

@app.route('/movies')
def all_movies():
    """view all movies"""

    movies = crud.get_movies()

    return render_template("all_movies.html", movies=movies)

@app.route("/movies/<movie_id>")
def show_movie(movie_id):
    """ Show details on a particular movie. """
    movie = crud.get_movie_by_id(movie_id)

    return render_template("movie_details.html", movie=movie)

@app.route('/users')
def all_users():
    """view all user"""

    users = crud.get_users()

    return render_template("all_users.html", users=users)

@app.route("/users", methods=["POST"])
def register_user():
    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if user:
        flash("you are already registred, try another email")

    else:
        crud.create_user(email, password)
        flash("Account has been created, login")

    return redirect("/")

@app.route("/login", methods = ["POST"])
def login_page(): 

    email = request.form.get("email")
    password = request.form.get("password")
    user = crud.get_user_by_email(email)

    if not user or user.password != password:
        flash("Incorrect password")
    else:
        session["user_email"] = user.email
        flash("Welcome back!")

    return redirect("/")

@app.route("/users/<user_id>")
def show_user(user_id):
    """ Show particular user page. """
    user = crud.get_user_by_id(user_id)

    return render_template("user_details.html", user=user)


if __name__ == "__main__":
    #DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
