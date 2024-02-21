from flask import Flask
from json import dumps
from ids import check


app = Flask(__name__)

@app.route('/check', methods=['POST'])
def make_check():
    check()

@app.route('/reports', methods=['GET'])
def recup_reports():
    essaie = {
        "data" : 10,
        "pasData" : 20
    }

    return dumps(essaie)


@app.route('/reports/<id>', methods=['GET'])
def recup_report_by_id():
    return "report_by_id"

@app.route('/reports/last', methods=['GET'])
def recup_report_by_id():
    return "Last report"


if __name__ == '__main__':
    app.run(host="0.0.0.0" , port=80)
