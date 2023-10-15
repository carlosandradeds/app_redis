from flask import Flask, request, render_template
import redis

app = Flask(__name__)

#Conecte ao servidor Redis
redis = redis.StrictRedis(host='localhost', port=6379, db=0)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/processar', methods=['POST'])
def processar():
    login = request.form['login']

    if redis.exists(login):
        resultado=f'Login Ativo, criado em {redis.get(login).decode("utf-8")}. Tempo para Expirar: {redis.ttl(login)} segundos'
    
    else:
        redis.set(login, 'Login Registrado', ex=10)
        resultado = 'Login Registrado'
    
    
    return resultado

if __name__ == '__main__':
    app.run()