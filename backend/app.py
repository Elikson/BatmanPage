import os
import requests
from flask import Flask, request, jsonify, json
from flask_cors import CORS, cross_origin

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/email/<email>/<mensagem>")
@cross_origin()
def enviar(email, mensagem):
    print("Executou a rota de email "+email+" "+mensagem)

    # create message object instance
    msg = MIMEMultipart()

    # setup the parameters of the message
    password = ""
    msg['From'] = ""
    msg['To'] = email
    msg['Subject'] = "Bat mensagem"

    # add in the message body
    msg.attach(MIMEText(mensagem, 'plain'))

    #create server
    server = smtplib.SMTP('smtp.url: port')
     
    server.starttls()
     
    # Login Credentials for sending the mail
    server.login(msg['From'], password)
     
     
    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
     
    server.quit()
    return "Bat mensagem enviada com sucesso!"

app.run(host="0.0.0.0", port = 2000, debug = False)
