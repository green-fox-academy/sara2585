from flask import Flask
from flask import render_template
app = Flask(__name__)

authors = [
    {
        "id": 100,
        "name": "John",
        "likes": [
            202,
            200
        ]
    },
    {
        "id": 101,
        "name": "jane",
        "likes" : [
            200
        ]
    }
]

posts = [
    {
        "id": 200,
        "author": 100,
        "content": "Difficulty on insensible reasonable in. From as went he they."
    },
    {
        "id": 201,
        "author": 100,
        "content": "Preference themselves me as thoroughly partiality considered on in estimating."
    },
    {
        "id": 202,
        "author": 101,
        "content": "In as name to here them deny wise this. As rapid woody my he me which."
    }
]




@app.route("/posts")
def list_posts():
    transformed_posts = []
    for post in posts:
        post_dic = {}
        post_dic["id"] = post["id"]
        post_dic["content"] = post["content"]
        post_dic["liked_by"] = []
        for author in authors:
            if author["id"] == post["author"]:
                post_dic["author"] = author["name"]
            for like in author["likes"]:
                if like == post["id"]:
                    post_dic["liked_by"].append(author["name"])
        transformed_posts.append(post_dic)
    #print(transformed_posts)
    return render_template("posts.html", posts=transformed_posts)