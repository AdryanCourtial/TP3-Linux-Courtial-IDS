from flask import Flask
from json import dumps
from ids import check, recup_db, path_to_last


app = Flask(__name__)

@app.route('/check', methods=['POST'])
def make_check():
    check()

@app.route('/reports', methods=['GET'])
def recup_reports():
    file = open("./data/report.json", "r")
    return file
    


@app.route('/reports/<id>', methods=['GET'])
def recup_report_by_id(id):
    file = open(f"./data/data_id/{id}.json", "r")
    return file


@app.route('/reports/last', methods=['GET'])
def recup_report_last():
    file = open(path_to_last, "r")
    return file


if __name__ == '__main__':
    app.run(host="0.0.0.0" , port=80)
