from flask import jsonify, Flask
app=Flask(__name__)
@app.route('/person/')
def hello():
    return jsonify({'name':"Reena",'address':'India'})
@app.route('/numbers/')
def print_list():
    return jsonify(list(range(5)))

app.run()