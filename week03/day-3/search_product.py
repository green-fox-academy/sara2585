from flask import Flask
from flask import render_template
from flask import request
import csv
app = Flask(__name__)

@app.route('/')
def search_input():
    return render_template('search.html')


@app.route('/result', methods=['POST'])
def search_product():
    f = open("product.csv")
    contents = csv.reader(f)
    products = []
    for product in contents:
        products.append((str(product[0]).split(";")))
    
    name = request.form.get('productname')
    price = request.form.get('pricename')
    qty = request.form.get('qty')
    result = []

    tmp_result = []
    if name is not None:
        for product in products:
            if name in product[1]:
                tmp_result.append(product)
    else:
        tmp_result = products
  
    tmp_result2 = []
    print(tmp_result)
    if price is not "":
        for product in tmp_result:
            if price == product[2]:
                tmp_result2.append(product)
    elif price is "":
        tmp_result2 = tmp_result

    if qty is not "":
        for product in tmp_result2:
            if qty == product[3]:
                result.append(product)
    else:
        result = tmp_result2
    print(result)

    result_list = []

    for item in result:
        result_list.append(";".join(item))

    return render_template('result.html', result_list=result_list)



    

