#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from flask import jsonify
from wiringx86 import GPIOGalileoGen2 as GPIO
app = Flask(__name__)

gpio = GPIO(debug=False)
dict(nome='quarto', status=1, id=1)
@app.route('/')
def hello_world():
    return render_template('info.html')

@app.route('/comodos',  methods=['POST', 'GET'])
def comodo():
    comodos = {
        'quarto': {'pin':13, 'id': 1, 'state':0},
        'sala': {'pin':7, 'id':2, 'state': 0},
        'cozinha': {'pin':9,'id':2, 'state': 0}
    }
    if request.method == 'POST':
        #aparelho = request.form['id_ap']
        id_ap = request.form['id_ap']
        acao = int(request.form['acao'])
        #dict(nome='quarto', status=1, id=1)

        if acao == 0:
            if (gpio.digitalRead(comodos[id_ap]['pin'])):
                gpio.digitalWrite(comodos[id_ap]['pin'], gpio.LOW)
                comodos[id_ap]['state'] = 0
            else:
                msg = 'O dispositivo está ligado'
        if acao == 1:
            if not(gpio.digitalRead(comodos[id_ap]['pin'])):
                gpio.digitalWrite(comodos[id_ap]['pin'], gpio.HIGH)
                comodos[id_ap]['state'] = 1
            else:
                msg = 'O dispositivo está desligado'
                print "sandro"
        templateData = {'id_ap': id_ap, 'msg': msg, 'estado': comodos[id_ap]['state']}

    return render_template('testeform.html', **templateData)
#codigo
@app.route('/codigo')
def hello_world2():
    return 'Hello World 2!'

@app.route('/_get_current_user')
def get_current_user():
    return jsonify(username='judison1',
                   email='teste@teste.com',
                   id=1)

@app.route('/get_dispositivos')
def get_dispositivos():
    return jsonify(comodo="sala",aparelhos=[dict(nome='teste',status=1,id=1),  dict(nome='teste2',status=0,id=2)])

if __name__ == '__main__':
    app.run()
    #app.run(host='10.42.0.1', port=8080, debug=True)