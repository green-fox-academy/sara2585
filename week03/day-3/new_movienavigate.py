from flask import Flask
from flask import render_template

app = Flask(__name__,static_url_path="/static")


@app.route('/')
def movie_navigate():
    return render_template('movieindex.html')



@app.route('/movie/<movie_id>')
def my_firstwebsite(movie_id):
    f = open(f"{movie_id}.txt") 
    contents = f.readlines()
    title = contents[0]
    description = contents[1]
    pic = contents[2]
    return render_template("index.html", title = title, description = description, pic = pic)