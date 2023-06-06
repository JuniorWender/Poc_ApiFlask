from flask import request, jsonify
from app import app

# @app.route('/teste', methods=['GET','POST'])
# def teste():
#     if request.method == 'GET':
#         return jsonify({'response': 'Get Request Called'})
#     elif request.method == 'POST':
#         req_Json = request.json()
#         name = req_Json['name']
#         return jsonify({'response': 'hi' + name})

@app.route('/auth', methods=['POST'])
def auth():
    applicationName = request.form['applicationName']
    applicationPassword = request.form['applicationPassword']
    print('nome: ',applicationName)
    print('senha: ',applicationPassword)