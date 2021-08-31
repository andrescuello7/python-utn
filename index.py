#llamado a lel framework Flask
from flask import Flask, render_template

#importar Flask
app = Flask(__name__)

#rutas de la pagina
@app.route('/')
def home():
    return render_template('index.html')

#servidor en funcionamiento
if __name__ == '__main__':
    app.run(port = 5000, debug = True)