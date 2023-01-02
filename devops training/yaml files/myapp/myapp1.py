from flask import *

app = Flask(__name__)
@app.route('/hello', methods=['GET','POST'])
def welcome():
    data_set="Hello Valtech"
    json_dump = json.dumps(data_set)
    return json_dump

if __name__ == '__main__':
    app.run(port=5000)
