from flask import Flask, send_from_directory, redirect
from pathlib import Path

app = Flask(__name__, static_folder=None)

# Caminho do HTML a ser servido
HTML_PATH = Path(__file__).parent / "power-bi-documentador/index.html"

@app.get("/")
def root():
    # Redireciona / para /home
    return redirect("/home", code=302)

@app.get("/home")
def home():
    # Serve o arquivo HTML diretamente
    return app.response_class(HTML_PATH.read_text(encoding="utf-8"), mimetype="text/html")

# Opcional: servir assets estáticos se o HTML referenciar css/js/imagens via caminhos relativos
@app.get("/assets/<path:filename>")
def assets(filename):
    assets_dir = HTML_PATH.parent
    return send_from_directory(assets_dir, filename)

if __name__ == "__main__":
    # Execução local
    app.run(host="0.0.0.0", port=8000)
