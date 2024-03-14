from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Obtener datos de la API
    api_url = 'https://dolar.melizeche.com/api/1.0/'
    response = requests.get(api_url)
    data = response.json()

    # Extraer datos específicos para mostrar en la página
    dolarpy_data = data.get('dolarpy', {})

    # Renderizar la plantilla HTML con los datos
    return render_template('index.html', dolarpy_data=dolarpy_data)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
