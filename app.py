from flask import Flask

app = Flask(__name__)
app.config.from_object('ext.configuration')

print('plot')
print(app.config['UPLOAD_PATH'])
print('-----------------------------')

if __name__ == '__main__':

    app.run(debug=True)
    