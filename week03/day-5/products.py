from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/products')
def list_products():
    Products = [
    ("Milk", 3.59123),
    ("Bread", 2.96332),
    ("Rice", 0.64111)]
    return render_template('show_products.html',products = Products)
