from flask import jsonify, Flask
app=Flask(__name__)
@app.route('/home/')
def home():
    return "Home page"
@app.route('/contact')
def contact():
    return "Conatct page"

app.run(port=8043)