#!flask/bin/python
from flask import Flask
from flask import request
from flask import abort
import time
import utils
app = Flask(__name__)
company_list = []
process = None

@app.route('/companyName', methods=['POST'])
def set_company_name():
    response_text = {}
    if not request.json:
        abort(400)
    else:
        company_name = request.json['text']
        company_list.append(company_name)
        global process
        if process == None:
            process = utils.proc_start(company_list)
        else:
            utils.proc_to_stop(process)
            process=None
            process = utils.proc_start(company_list)
        response_text['Message'] = "Company Added"
    return response_text, 201

@app.route("/")
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    app.run(debug=True)