from flask import Flask
from ids import check

app = Flask(__name__)

app.route('/check', methods=['POST'])
def make_check():
    check()

app.route('/reports', methods=['GET'])
def recup_reports():
    ...


app.route('/reports/<id>', methods=['GET'])
def recup_report_by_id():
    ...