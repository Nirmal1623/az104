from flask import *
import json, time

app=Flask(__name__)
@app.route('/',methods=['GET'])
def home_page():
    data_set={'page': 'home', 'message': 'successfully loaded the page', 'Timestamp' : time.time()}
    json_dump = json.dumps(data_set)
    return json_dump

@app.route('/',methods=['GET'])
def request_page():
    user_query = str(request.args.get('user')) #/user
    data_set={'page':'Request','Message':'Successfully got the request for {user_query}','Timestamp':time.time()}
    json_dump = json.dumps(data_set)
    return json_dump

if __name__ == '__main__':
    app.run(port=7777)