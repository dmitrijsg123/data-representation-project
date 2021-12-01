from flask import Flask, url_for,redirect,abort, request, jsonify
from StockDao import stockDao

app = Flask(__name__,static_url_path='',static_folder='staticpages') 


@app.route('/')     
def index():
    return "hello"


@app.route('/stock')     
def getAll():
    return jsonify(stockDao.getAll())


@app.route('/stock/<int:Item_number>')     
def findById(Item_number):
    return jsonify(stockDao.findById(Item_number))


@app.route('/stock',methods=['POST'])     
def create():
    if not request.json:
        abort(400)

    stock = {
        "Item_number": request.json["Item_number"],
        "Item_name": request.json["Item_name"], 
        "supplier": request.json["supplier"],
        "Price": request.json["Price"]
    }
    return jsonify(stockDao.create(stock))


@app.route('/stock/<int:Item_number>',methods=['PUT'])     
def update(Item_number):
    found = stockDao.findById(Item_number)
    if len(found) == {}:
        return jsonify({}), 404
    current = found
    if 'Item_name' in request.json:
        current['Item_name'] = request.json['Item_name']

    if 'supplier' in request.json:
        current['supplier'] = request.json['supplier'] 

    if 'Price' in request.json:
        current['Price'] = request.json['Price'] 
    stockDao.update(current)
    
    return jsonify(current)


@app.route('/stock/<int:Item_number>',methods=['DELETE'])     
def delete(Item_number):
    stockDao.delete(Item_number)
    
    return jsonify({"done":True})


if __name__ == '__main__':
    print("in if")
    app.run(debug=True)                       # run Flask