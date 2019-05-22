from flask import Flask
from flask import render_template

app = Flask(__name__,static_url_path="/static")


@app.route('/')
def movie_navigate():
    return render_template('movieindex.html')



@app.route('/<movie_id>')
def my_firstwebsite(movie_id):
    movie_dic = {"01": "movie1.html", "02":"movie2.html", "03": "movie3.html", "04": "movie4.html", "05": "movie5.html"}   
    return render_template(movie_dic[movie_id])