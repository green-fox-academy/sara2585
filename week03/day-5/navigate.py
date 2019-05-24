from flask import Flask
from flask import render_template
import random

app = Flask(__name__)

@app.route('/1')
def hello_john():
    greetings = ['Hello,John!', 'Hi, John!', 'How are you today?']
    greeting = random.choice(greetings)
    return render_template('Greet_john.html', greeting = greeting)

@app.route('/2')
def hello_john2():
    greetings = ['Hello,', 'Hi, ', 'How are you today?']
    names = ['john', 'lucy', 'david']
    greeting = random.choice(greetings)
    name = random.choice(names)
    return render_template('Greet_John2.html', greeting = greeting, name = name)

@app.route('/products')
def list_products():
    Products = [
    ("Milk", 3.59123),
    ("Bread", 2.96332),
    ("Rice", 0.64111)]
    return render_template('show_products.html',products = Products)

articles = [
    {
        "content": "Ne istas culpa ha im negat de. Ii perductae evertenda at desuescam. Nudi per ita sui dare ideo sola omne ordo. Sui sex item sane quum. Paucos sicuti tot qui tantae aliquo strata iis tantas. Mo purgantur at affirmans im reddendum co. Pleraque videntur ut ideamque imaginem ha.",
        "seen": ["John", "Jane", "Bob"]
    },
    {
        "content": "Aliud curam seu venti nihil sed istud volui eae qua. Autho ha falsi fidam tangi ut an tactu. Revera per eandem vox coelum videbo nam virtus. Item olim ei se duas ut. Ut mo ut peccato student adorare et diversa. Praecipuis ad conjunctam me percipitur agnoscerem at perfectius respondere. Horum meo porro uno debeo. Fallacem sentiens ha expertus delapsus dubitare ii. Ex ii efficiente et to perspicuae voluptatem arbitrabar.",
        "seen": ["John", "Jane"]
    },
    {
        "content": "Credendi at nequidem exhibere de. Debeo me dicam ex at ferri digna. Coloribus differant disputari vix cogitandi jam stabilire. Perfacile ut reliquiae perfectae ut. Fuisse falsas captum cui volent notior verbis sui. Meam idem nam ope prae isti quia jure hac. Lor durent has secius fronte usu auditu sumpti. Falso nomen aliud vim calor jam alias annos ubi. Movendi sum creatus vim fas majorem attendo propter. Sui videamus uno profecto refutent rom notitiam innumera potuerit.",
        "seen": ["John"]
    },
    {
        "content": "Potui habeo visus ens mea. An vi re continetur me familiarem negationem. Rei inveniri jam viderunt subducam tam imponere jam. Sub cui more ipsi meum.",
        "seen": []
    }
]

@app.route("/articles")
def list_articles():
    return render_template("articles.html", articles=articles)

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


@app.route('/')
def home():
    return render_template("base.html")
