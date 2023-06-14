import json
from flask import Flask,jsonify,request

import datetime
import jwt # Cria o token
from jwt.exceptions import InvalidTokenError #Para lançar o erro de token inválido
import os # Mexe com arquivos

# --------------------------------------------------------------------------------------

# navio.nome = 'Kang Cheng 1'
# navio.quantidade_poroes = 5
# navio.comprimento_trapezio_proa = 28
# navio.comprimento_retangular_proa = 10
# navio.comprimento_trapezio_popa = 28
# navio.comprimento_retangular_popa = 10
# navio.largura_popa = 12
# navio.largura_proa = 11
# navio.meia_nau = 23
# navio.tank_top = [25,18 ,26, 18, 25]
# navio.comprimentos_poroes = [28,28,28,28,28]
# navio.larguras_escotilhas = [18,18,18,18,18]
# navio.comprimentos_escotilhas = [ 17, 17,17, 17,19]

# -------------------------------- Classes --------------------------------
class Navio:
    def __init__(self, nome, quantidade_poroes, comprimento_trapezio_proa, comprimento_retangular_proa, comprimento_trapezio_popa, comprimento_retangular_popa, largura_popa, largura_proa, meia_nau, tank_top, comprimentos_poroes, larguras_escotilhas, comprimentos_escotilhas):
        self.nome = nome
        self.quantidade_poroes = int(quantidade_poroes)
        self.comprimento_trapezio_proa = int(comprimento_trapezio_proa)
        self.comprimento_retangular_proa = int(comprimento_retangular_proa)
        self.comprimento_trapezio_popa = int(comprimento_trapezio_popa)
        self.comprimento_retangular_popa = int(comprimento_retangular_popa)
        self.largura_popa = int(largura_popa)
        self.largura_proa = int(largura_proa)
        self.meia_nau = int(meia_nau)
        self.tank_top = [int(item) for item in tank_top.strip('][').split(',')]
        self.comprimentos_poroes = [int(item) for item in comprimentos_poroes.strip('][').split(',')]
        self.larguras_escotilhas = [int(item) for item in larguras_escotilhas.strip('][').split(',')]
        self.comprimentos_escotilhas = [int(item) for item in comprimentos_escotilhas.strip('][').split(',')]


app = Flask(__name__)
app.config.from_object('ext.configuration')

print('plot')
print(app.config['UPLOAD_PATH'])

print('-----------------------------')

# -------------------------------- Rotas de Autenticação --------------------------------
# @app.route('/auth', methods=['POST'])
# def auth():
#     recived = request.get_json()
#     applicationName = recived['applicationName']
#     applicationPassword = recived['applicationPassword']
#     payload = {'user': applicationName, 'password': applicationPassword, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}

#     print('nome: ',applicationName)
#     print('senha: ',applicationPassword)

#     jwt = createJwtToken(payload)
#     return jsonify({'token': jwt})

# def createJwtToken(payload):
#     token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
#     return token

# def decodeJwtToken(token):
#     try:
#         payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
#         return payload
#     except InvalidTokenError:
#         return None
    
@app.route('/cargoPlan', methods=['POST','GET'])
def validateJWT():
    
    # token = request.headers.get('Authorization')

    # if not token:
    #     return jsonify({'error': 'Erro, Você deve enviar o Token'}), 401
    
    # token = token.split('Bearer ')[-1]  # Remove o prefixo 'Bearer' do token

    # payload = decodeJwtToken(token)
    # if not payload:
    #     return jsonify({'message': 'Erro, Token Inválido'}), 401

    if request.method == 'POST':
        navio = Navio(request.form['nome'], request.form['quantidade_poroes'], request.form['comprimento_trapezio_proa'], request.form['comprimento_retangular_proa'], request.form['comprimento_trapezio_popa'], request.form['comprimento_retangular_popa'], request.form['largura_popa'], request.form['largura_proa'], request.form['meia_nau'], request.form['tank_top'], request.form['comprimentos_poroes'], request.form['larguras_escotilhas'], request.form['comprimentos_escotilhas'])
        # x = request.files
        
        print('navio: ', navio.nome)
        # print('arquivo: ', arquivo.filename)
        # print('navio',Navio.getlargura_escotilhas())
        # print('navio',Navio.getFile())
        # validatePost(Navio)

    # if request.method == 'GET':
    #     #Retorna se o processo do cargo plan já foi finalizado ou não
    #     verifyProcess(payload)

    return jsonify({'message': 'Token Valido'}), 200


# -------------------------------- Rotas de Envio de informação para o cargoPlan --------------------------------

def createCargoPlan(body):
    # file = body['file']

    # file_name = 'inputs.csv'
    # file_path = app.config['UPLOAD_PATH'] + '/' + file_name

    # if not os.path.exists(file_path):
    #     os.makedirs(file_path)

    # file_path = os.path.join(app.config['UPLOAD_PATH'], file_name)
    # file.save(file_path)

    return jsonify({'message': 'CargoPlan criado com sucesso'}), 200

def verifyProcess(payload):
    #Verifica se o processo do cargo plan já foi finalizado ou não
    #Se já foi finalizado, retorna o arquivo de saída
    #Se não foi finalizado, retorna uma mensagem de erro
    return jsonify({'message': 'CargoPlan criado com sucesso'}), 200


if __name__ == '__main__':

    app.run(debug=True, port=5001)
    