from flask import Flask
from flask import request

import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/tester')
def tester():
    url = 'http://127.0.0.1:5000/test'
    myobj = {'string_to_cut': 'iamyourlyftdriver'}
    x = requests.post(url, data = myobj)
    print(x.text)
    return 'Done'

@app.route('/test', methods=['POST'])
def main():
    my_new_str = ''
    if request.method == 'POST':
        myStr = request.form['string_to_cut']
    for i in range(2, len(myStr)):
        if ((i+1) % 3 == 0):
            my_new_str += myStr[i]
    myObj = {'return_string':my_new_str}
    return json.dumps(myObj)

if __name__ == "__main__":
    app.run()