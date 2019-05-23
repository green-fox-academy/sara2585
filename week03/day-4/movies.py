from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify, make_response
import csv

app = Flask(__name__)

@app.route('/api/movies')
def get_movies():
    f = open("movies.csv",'r')
    contents = csv.reader(f)

    movies = []
    for movie in contents:
        movies.append(movie)
    # print(movies)
    f.close()
    dir = []
    for movie in movies:
        movie_dic = {}
        movie_dic["id"] = movie[0]
        movie_dic['title'] = movie[1]
        movie_dic['year'] = movie[2]
        movie_dic['genre'] = movie[3]
        movie_dic['description'] = movie[4]
        dir.append(movie_dic)
    reponse = jsonify(dir)
    return reponse

@app.route('/api/movies/<movie_id>')
def get_one_movie(movie_id):
    f = open("movies.csv",'r')
    contents = csv.reader(f)

    movies = []
    for movie in contents:
        movies.append(movie)
    # print(movies)
    f.close()

    target_movie=[]
    target_movie_dic = {}
    for movie in movies:
        if movie[0] == movie_id:
            target_movie = movie

    # print(target_movie)
    # print(target_movie[1])

    target_movie_dic["id"] = target_movie[0]
    target_movie_dic["title"] = target_movie[1]
    target_movie_dic["year"] = target_movie[2]
    target_movie_dic["genre"] = target_movie[3]
    target_movie_dic["description"] = target_movie[4]

    reponse = jsonify(target_movie_dic)
    return reponse

@app.route('/api/movies', methods=["POST"])
def add_movies():
    set_key = "sarakey"
    
    headers = request.headers
    given_key = headers.get('app-key')
    movie = []
    body = request.get_json()
    with open('movies.csv','r') as f:
        contents = csv.reader(f)
        n = 0
        for content in contents:
            n += 1
        next_id = n + 1

    new_movie = []

    if given_key == set_key:
        body['id'] = next_id
        reponse = jsonify(body)
        # print(body)
        new_movie.append(body['id'])
        new_movie.append(body['title'])
        new_movie.append(body['year'])
        new_movie.append(body['genre'])
        new_movie.append(body['description'])
        # print(new_movie)
        out = open('movies.csv', 'a', newline='')
        csv_write = csv.writer(out)
        csv_write.writerow(new_movie)
        return reponse
    else:
        reponse = make_response(jsonify(error = 'Invalid API_KEY'))
        reponse.status_code = 403
        return reponse


@app.route('/api/movies/<movie_id>', methods=["PUT"])
def update_movie(movie_id):
    set_key = "sarakey"
    
    headers = request.headers
    given_key = headers.get('app-key')
    movie = []
    body = request.get_json()

    f = open("movies.csv",'r')
    contents = csv.reader(f)

    movies = []

    for movie in contents:
        movies.append(movie)
    
    #print(movies)
    f.close()
    replace_line = 10000000
    replace_movie = []
   
    for i in range(len(movies)):
        # print(type(movies[i][0]))
        # print(type(movie_id))
        if movies[i][0] == movie_id:
            replace_line = i

    if given_key == set_key and replace_line != 10000000:
        replace_movie.append(movie_id)
        replace_movie.append(body['title'])
        replace_movie.append(body['year'])
        replace_movie.append(body['genre'])
        replace_movie.append(body['description'])
        movies[replace_line] = replace_movie
        out = open('movies.csv', 'w', newline='')
        csv_write = csv.writer(out)
        for movie in movies:
            print(movie)
            csv_write.writerow(movie)
        body['id'] = movie_id
        reponse = jsonify(body)
        return reponse

    elif given_key != set_key:
        reponse = make_response(jsonify(error = 'Invalid API_KEY'))
        reponse.status_code = 403
        return reponse

    else:
        reponse = make_response(jsonify(error = f'No movie found with {movie_id} ID'))
        reponse.status_code = 404
        return reponse

@app.route('/api/movies/<movie_id>', methods=["DELETE"])
def delete_movie(movie_id):
    set_key = "sarakey"
    print("successsssssssssssssssssssssssssss")
    headers = request.headers
    given_key = headers.get('app-key')
    movie = []

    f = open("movies.csv",'r')
    contents = csv.reader(f)

    movies = []
    for movie in contents:
        movies.append(movie)
    
    #print(movies)
    f.close()
    delete = False
    id_list = []
    for movie in movies:
        id_list.append(movie[0])
    if movie_id in id_list:
        delete = True
    
    new_movies = []
    # print(delete)

    for i in range(len(movies)):
        if movies[i][0] != movie_id:
            new_movies.append(movies[i])
    
    if given_key == set_key and delete:
        out = open('movies.csv', 'w', newline='')
        csv_write = csv.writer(out)
        for movie in new_movies:
            print(movie)
            csv_write.writerow(movie)
        reponse = jsonify("Delete succeed!")
        return reponse

    elif given_key != set_key:
        reponse = make_response(jsonify(error = 'Invalid API_KEY'))
        reponse.status_code = 403
        return reponse

    else:
        reponse = make_response(jsonify(error = f'No movie found with {movie_id} ID'))
        reponse.status_code = 404
        return reponse




         



