from flask import Flask, render_template, jsonify
import cv2
import os

app = Flask(__name__)

# Ruta del archivo
dataPath = 'C:/Users/USUARIO/Downloads/miproyecto/Data'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/capturar-rostros')
def capturar_rostros():
    
    os.system("python capturandoRostros.py")  
    return jsonify({'status': 'Rostros capturados'})

@app.route('/reconocer-emociones')
def reconocer_emociones():
    os.system("python reconocimientoEmociones.py")  
    return jsonify({'status': 'Reconocimiento de emociones iniciado'})

if __name__ == "__main__":
    app.run(debug=True)
