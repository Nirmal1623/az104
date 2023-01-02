from flask import jsonify, Flask
app=Flask(__name__)
@app.route('/coffeebeans/')
def coffee():
    return "coffee", 418

app.run(port=8043)