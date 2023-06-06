from flask import Flask,jsonify,request

import datetime
import jwt # Cria o token
from jwt.exceptions import InvalidTokenError #Para lançar o erro de token inválido
import os # Mexe com arquivos

app = Flask(__name__)
app.config.from_object('ext.configuration')

print('plot')
print(app.config['UPLOAD_PATH'])
print('-----------------------------')


# -------------------------------- Rotas de Autenticação --------------------------------
@app.route('/auth', methods=['POST'])
def auth():
    recived = request.get_json()
    applicationName = recived['applicationName']
    applicationPassword = recived['applicationPassword']
    payload = {'user': applicationName, 'password': applicationPassword, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}

    print('nome: ',applicationName)
    print('senha: ',applicationPassword)

    jwt = createJwtToken(payload)
    return jsonify({'token': jwt})

def createJwtToken(payload):
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    return token

def decodeJwtToken(token):
    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        return payload
    except InvalidTokenError:
        return None
    
@app.route('/cargoPlan', methods=['POST','GET'])
def validateJWT():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'error': 'Erro, Você deve enviar o Token'}), 401
    
    token = token.split('Bearer ')[-1]  # Remove o prefixo 'Bearer' do token

    payload = decodeJwtToken(token)
    if not payload:
        return jsonify({'message': 'Erro, Token Inválido'}), 401

    if request.method == 'POST':
        body = request.get_json()
        if not body:
            return jsonify({'message': 'Erro, Você deve enviar o corpo da requisição'}), 401
        
        print('body: ',body)
        validatePost(body)

    if request.method == 'GET':
        #Retorna se o processo do cargo plan já foi finalizado ou não
        verifyProcess(payload)

    return jsonify({'message': 'Token Valido'}), 200


# -------------------------------- Rotas de Envio de informação para o cargoPlan --------------------------------
def validatePost(body):
    if not body['width']:
        return jsonify({'message': 'Erro, Você deve enviar a largura'}), 400
    if not body['height']:
        return jsonify({'message': 'Erro, Você deve enviar o comprimento'}), 400
    # if not body['file']:
    #     return jsonify({'message': 'Erro, Você deve enviar o arquivo'}), 400

    createCargoPlan(body,token)


def createCargoPlan(body):
    width = body['width']
    height = body['height']
    # file = body['file']

    # file_name = 'inputs.csv'
    # file_path = app.config['UPLOAD_PATH'] + '/' + file_name

    # if not os.path.exists(file_path):
    #     os.makedirs(file_path)

    # file_path = os.path.join(app.config['UPLOAD_PATH'], file_name)
    # file.save(file_path)

    print('largura: ',width)
    print('comprimento: ',height)

    return jsonify({'message': 'CargoPlan criado com sucesso'}), 200

def verifyProcess(payload):
    #Verifica se o processo do cargo plan já foi finalizado ou não
    #Se já foi finalizado, retorna o arquivo de saída
    #Se não foi finalizado, retorna uma mensagem de erro
    return jsonify({'message': 'CargoPlan criado com sucesso'}), 200



if __name__ == '__main__':

    app.run(debug=True, port=5001)
    